from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import BookViewSet 

#urls.py
router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    # path('register', signup, name='register'),
    # path('login', login, name='login'),
    # path('token', test_token, name='token'),
    path('', include(router.urls)),
]