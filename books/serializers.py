from rest_framework import serializers
from .models import Book, Category
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
 
   


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        modek = Category
        fields = '__all__'
        

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'        # fields = ['id', 'title', 'author', 'price', 'created_at', 'updated_at']

        