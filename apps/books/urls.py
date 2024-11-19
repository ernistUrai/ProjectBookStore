from django.urls import path, include

from .views import *

urlpatterns = [
    path('books/', BookListCreateAPiView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='books'),
    path('books/search/', BookSearchView.as_view(), name='serch'),
]