
from django.urls import path, include

from .views import *

urlpatterns = [
    path('books/', BookListCreateAPiView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('books/authors/', AuthorListAPIView.as_view(), name='authors'),
    path('books/favorite/', FavoriteBookView.as_view(), name="favorite"),
    path('books/favorite/', FavoriteBookView.as_view(), name="favorite"),


    path('books/search/', BookSearchView.as_view(), name='search'),
    path('books/orders/', OrderView.as_view(), name="orders"),
    path('books/orders/<int:pk>/', UserOrderListView.as_view(), name="orders_user_list"),
    path('books/<int:book_id>/coments/', ComentBookAPIView.as_view(), name="coments"),
    
]

