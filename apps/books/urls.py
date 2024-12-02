
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register(r'books', BookListApiView, basename='book-list')
router.register(r'authors', AuthorListAPIView ) 
router.register(r'cart', CartAPIView)
router.register(r'cart-items', CartItemAPIView)
router.register(r'orders', OrderAPIView)
# router.register(r'favorite', FavoriteBookView)
# router.register(r'search', BookSearchView)
# router.register(r'orders', OrderView)
# router.register(r'orders/<int:pk>', UserOrderListView)
router.register(r'coments', ComentBookAPIView)

urlpatterns = [
    path('', include(router.urls)),
]




# urlpatterns = [
#     path('books/', BookListCreateAPiView.as_view(), name='books'),
#     path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
#     path('books/authors/', AuthorListAPIView.as_view(), name='authors'),
#     path('books/favorite/', FavoriteBookView.as_view(), name="favorite"),
#     path('books/favorite/', FavoriteBookView.as_view(), name="favorite"),


#     path('books/search/', BookSearchView.as_view(), name='search'),
#     path('books/orders/', OrderView.as_view(), name="orders"),
#     path('books/orders/<int:pk>/', UserOrderListView.as_view(), name="orders_user_list"),
#     path('books/<int:book_id>/coments/', ComentBookAPIView.as_view(), name="coments"),
    
# ]

