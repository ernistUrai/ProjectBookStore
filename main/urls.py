from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls'), name='api'),
    path('users/', include('users.urls'), name='api'),
]
