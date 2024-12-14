
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *
from .filters import BookFilter

router = DefaultRouter()

router.register(r'books', BookListAPIView, basename='book-list')
router.register(r'authors', AuthorListAPIView ) 
router.register(r'coments', ComentBookAPIView, basename='coment-book')
router.register(r'cart', CartAPIView)
router.register(r'cart-items', CartItemAPIView)
router.register(r'orders', OrderAPIView)
urlpatterns = [
    path('', include(router.urls)),
]




