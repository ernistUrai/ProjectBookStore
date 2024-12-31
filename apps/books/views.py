from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend
from .filters import BookFilter
from .models import Book, Order, ComentBook, Author, Cart, CartItem
from .serializers import BookSerializer, OrderSerializer, ComentBookSerializer, AuthorSerializer, CartSerializer, CartItemSerializer




class AuthorListAPIView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def retrieve(self, request, *args, **kwargs):
        author = self.get_object()
        author_serializer = self.get_serializer(author)
        books = author.books.all()
        book_serializer = BookSerializer(books, many=True)
        
        response_data = author_serializer.data
        response_data['books'] = book_serializer.data
        return Response(response_data, status=status.HTTP_200_OK)
        
    


class BookListAPIView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend] 
    filterset_class = BookFilter
    
    def retrieve(self, request, *args, **kwargs):
        book = self.get_object()
        book_serializer = self.get_serializer(book)
        coments = book.coments.all()
        coment_serializer = ComentBookSerializer(coments, many=True)
        
        response_data = book_serializer.data
        response_data['coments'] = coment_serializer.data
        return Response(response_data, status=status.HTTP_200_OK)
     
    
    
class ComentBookAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    queryset = ComentBook.objects.all()
    serializer_class = ComentBookSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    
    
class CartAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Cart.objects.filter(user=self.request.user)
        return Cart.objects.none()
    
    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return Response(
                {'message': 'Вы не авторизованы'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        if Cart.objects.filter(user=request.user).exists():
            return Response(
                {'message': 'Вы уже в корзине'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().create(request, *args, **kwargs)
    
    
    
class CartItemAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    
    
    
class OrderAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
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

    