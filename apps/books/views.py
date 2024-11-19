from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q

from .models import Book, Order
from .serializers import BookSerializer, OrderSerializer



class BookListCreateAPiView(generics.ListCreateAPIView):
  
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

# Поиск 
class BookSearchView(APIView):
    def get(self, request):
        search = request.GET.get('search')
       
        if not search:
            return Response({'message': 'Поисковое слово не может быть пустым!'}, status=status.HTTP_400_BAD_REQUEST)
        
        books = Book.objects.filter(
            Q(title__icontains=search) | Q(author__icontains=search) | Q(description__icontains=search) | Q(price__icontains=search)
        )
        
        if not books:
            return Response({'message': 'Ничего не найдено'})
        
        
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
# Класс для создания заказа
class Orderview(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        books = request.data.get('books', []) 
        delivery_address = request.data.get('delivery_address')
        
        book_objects = Book.objects.filter(id__in=books)
        
        if not book_objects.exists():
            return Response({"error": "Китептер табылган жок."}, status=status.HTTP_400_BAD_REQUEST)
        
        total_price = sum([book.price for book in book_objects])
        
        order = Order.objects.create(
            user=request.user,
            delivery_address=delivery_address,
            total_price=total_price,
            paiment_status='pending'
        )
        
        order.books.set(book_objects)
        order.save()
        
        serrializer = OrderSerializer(order)
        return Response(serrializer.data, status=status.HTTP_201_CREATED)
    

# Смотреть список заказов
class UserOrderListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        order = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)