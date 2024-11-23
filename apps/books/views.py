from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q

from .models import Book, Order, ComentBook
from .serializers import BookSerializer, OrderSerializer, ComentBookSerializer



class BookListCreateAPiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get(self, request, *args, **kwargs):
        book = self.get_object() 
        book_serializer = self.get_serializer(book) 
        comments = book.comments.all() 
        comment_serializer = ComentBookSerializer(comments, many=True) 
        
        response_data = book_serializer.data
        response_data['comments'] = comment_serializer.data
        
        return Response(response_data)
    
    
class ComentBookAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response({'message': 'Книга не найдена'}, status=status.HTTP_404_NOT_FOUND)
        
        coment_book = ComentBook.objects.filter(book=book)
        serializer = ComentBookSerializer(coment_book, many=True)  # Сериализатордун атын текшериңиз
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response({'message': 'Книга не найдена'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ComentBookSerializer(data=request.data)  # Сериализатордун атын текшериңиз
        if serializer.is_valid(): 
            serializer.save(book=book)  # book параметрин сактоо
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
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




   