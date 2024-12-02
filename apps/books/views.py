from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


from django.db.models import Q

from .models import Book, Order, ComentBook, Author, Cart, CartItem
from .serializers import BookSerializer, OrderSerializer, ComentBookSerializer, AuthorSerializer, CartSerializer, CartItemSerializer




class AuthorListAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def retrieve(self, request, *args, **kwargs):
        author = self.get_object()
        author_serializer = self.get_serializer(author)
        books = author.aut_books.all()
        book_serializer = BookSerializer(books, many=True)
        
        response_data = author_serializer.data
        response_data['books'] = book_serializer.data
        return Response(response_data, status=status.HTTP_200_OK)
        

    


class BookListApiView(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def retrieve(self, request, *args, **kwargs):
        book = self.get_object()
        book_serializer = self.get_serializer(book)
        coments = book.coments.all()
        coment_serializer = ComentBookSerializer(coments, many=True)
        
        response_data = book_serializer.data
        response_data['coments'] = coment_serializer.data
        return Response(response_data, status=status.HTTP_200_OK)
    

    
    

    
    
   
    
    
class ComentBookAPIView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    queryset = ComentBook.objects.all()
    serializer_class = ComentBookSerializer
    
    
    
class CartAPIView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
class CartItemAPIView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    
class OrderAPIView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
    
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Order.objects.filter(user=user)
        return Order.objects.none()
    
   
    
    
# # Поиск 
# class BookSearchView(APIView):
#     def get(self, request):
#         search = request.GET.get('search')
       
#         if not search:
#             return Response({'message': 'Поисковое слово не может быть пустым!'}, status=status.HTTP_400_BAD_REQUEST)
        
#         books = Book.objects.filter(
#             Q(title__icontains=search) | Q(author__icontains=search) | Q(description__icontains=search) | Q(price__icontains=search)
#         )
        
#         if not books:
#             return Response({'message': 'Ничего не найдено'})
        
        
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
    
# # Класс для создания заказа
# class OrderView(APIView):
#     permission_classes = [IsAuthenticated]
    
#     def post(self, request, *args, **kwargs):
#         books = request.data.get('books', [])
#         delivery_address = request.data.get('delivery_address')
        
#         book_objects = Book.objects.filter(id__in=books)
        
#         if not book_objects.exists():
#             return Response({"error": "Китептер табылган жок."}, status=status.HTTP_400_BAD_REQUEST)
        
#         total_price = sum([book.price for book in book_objects])
        
#         order = Order.objects.create(
#             user=request.user,
#             delivery_address=delivery_address,
#             total_price=total_price,
#             payment_status='pending' 
#         )
        
#         order.books.set(book_objects)
#         order.save()
        
#         serializer = OrderSerializer(order)  
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    

# # Смотреть список заказов
# class UserOrderListView(APIView):
#     permission_classes = [IsAuthenticated]
    
#     def get(self, request, *args, **kwargs):
#         order = Order.objects.filter(user=request.user)
#         serializer = OrderSerializer(order, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    
# # Довать книгу в избранное
# class FavoriteBookView(APIView):
#     permission_classes = [IsAuthenticated]
    
#     def get(self, request):
#         favorite_books = FavoriteBook.objects.filter(user=request.user)
#         serializer = FavoriteBookSerializer(favorite_books, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         book_id = request.data.get('book')
#         try:
#             book = Book.objects.get(id=book_id)
#         except Book.DoesNotExist:
#             return Response(
#                 {'message': 'Книга не найдена'},
#                 status=status.HTTP_404_NOT_FOUND
#             )
        
#         favorite, create = FavoriteBook.objects.get_or_create(user=request.user, book=book)
#         if not create:
#             return Response(
#                 {'message': 'Книга уже добавлена в избранное'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
        
#         serializer = FavoriteBookSerializer(favorite)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         def delete(self, request):
#             book_id = request.data.get('book')
#             try:
#                 favorite = FavoriteBook.objects.get(user=request.user, book=book_id)
#             except Book.DoesNotExist:
#                 return Response(
#                     {'message': 'Книга не найдена'},
#                     status=status.HTTP_404_NOT_FOUND
#                 )
#             favorite.delete()
#             return Response(
#                 {'message': 'Книга успешно удалена из избранного'},
#                 status=status.HTTP_204_NO_CONTENT
#             )
