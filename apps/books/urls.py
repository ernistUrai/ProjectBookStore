
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register(r'books', BookListAPIView, basename='book-list')
router.register(r'authors', AuthorListAPIView ) 
router.register(r'coments', ComentBookAPIView, basename='coment-book')
router.register(r'cart', CartAPIView)
router.register(r'cart-items', CartItemAPIView)
router.register(r'orders', OrderAPIView)
router.register(r'search', BookSearchView, basename='search')

urlpatterns = [
    path('', include(router.urls)),
]




