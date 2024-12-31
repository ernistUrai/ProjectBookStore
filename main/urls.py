from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .swagger import urlpatterns as swagger_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.books.urls'), name='api'),
    path('api/auth/', include('apps.users.urls'), name='api'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += swagger_urlpatterns
