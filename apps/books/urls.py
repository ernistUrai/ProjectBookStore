
from django.urls import path, include

from .views import *

urlpatterns = [
    path('books/', BookListCreateAPiView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='books'),

    path('books/search/', BookSearchView.as_view(), name='serch'),
    path('books/orders/', Orderview.as_view(), name="orders"),
    path('books/orders/<int:pk>/', UserOrderListView.as_view(), name="orders_user_list"),
    path('books/<int:book_id>/coments/', ComentBookAPIView.as_view(), name="coments"),
]