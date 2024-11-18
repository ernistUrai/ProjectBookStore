from django.conf import settings
from django.db import models
from rest_framework.authtoken.models import Token as DefaultToken

class Token(DefaultToken):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)