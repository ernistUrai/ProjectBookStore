from rest_framework import serializers
from .models import Book, Category, Order, ComentBook, Author, CartItem, Cart




class ComentBookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ComentBook
        fields = '__all__'
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        

class BookSerializer(serializers.ModelSerializer):
    coment = ComentBookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Book
        fields = '__all__' 
        

class AuthorSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author  
        fields = '__all__'
    

class OrderSerializer(serializers.ModelSerializer): 
        
    class Meta:
        model = Order
        fields = '__all__'
    
    
class CartItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CartItem
        fields = '__all__'
        
class CartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cart
        fields ='__all__'
    
    