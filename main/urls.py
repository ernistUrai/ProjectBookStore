from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/auth/', include('djoser.urls')),
    path('api/auth/token/', include('djoser.urls.jwt')),
    
    
    
    path('api/', include('apps.books.urls'), name='api'),
    path('', include('apps.users.urls'), name='api')
    
]
