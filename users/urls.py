from django.urls import path
from .views import *


urlpatterns = [
    path('api/signup/', signup, name='signup'),
    path('api/login/', login, name='login'),
    path('api/test_token/', test_token, name='test_token'),
]