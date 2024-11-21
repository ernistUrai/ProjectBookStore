from rest_framework import serializers
from .models import Book, Category, Order, ComentBook   
from apps.users.serializers import UserSerializer


class ComentBookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ComentBook
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    comments = ComentBookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = '__all__'
        

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