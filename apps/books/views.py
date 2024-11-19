from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import status

from django.db.models import Q

from .models import Book
from .serializers import BookSerializer



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