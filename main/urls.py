from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('apps.books.urls'), name='api'),
    path('users/', include('apps.users.urls'), name='api'),
]
