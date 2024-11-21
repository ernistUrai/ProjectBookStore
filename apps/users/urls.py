from django.urls import path
from .views import *


urlpatterns = [
    path('auth/register/', signup, name='signup'),
    path('auth/login/', login, name='login'),
    path('auth/test_token/', test_token, name='test_token'),
]

