from rest_framework import serializers
from .models import Book, Category, Order, ComentBook, Author, FavoriteBook
from apps.users.serializers import UserSerializer


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author  
        fields = '__all__'



class ComentBookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ComentBook
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
        

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'     


class OrderSerializer(serializers.ModelSerializer): 
    user = UserSerializer()
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = '__all__'
        
        
class FavoriteBookSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    book = BookSerializer()
    
    class Meta:
        model = FavoriteBook
        fields = '__all__'