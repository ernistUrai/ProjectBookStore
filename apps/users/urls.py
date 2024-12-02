from django.urls import path
from .views import *


urlpatterns = [
    path('register/', signup, name='signup'),
    path('login/', login, name='login'),
    path('test_token/', test_token, name='test_token'),
]

