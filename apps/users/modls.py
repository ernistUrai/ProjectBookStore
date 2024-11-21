from django.db import models
from django.contrib.auth.models import User
from books.models import Book


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField('Номер телефон', max_length=100, blank=True) 
    address = models.CharField('Адрес', max_length=100, blank=True)
    favorite_book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True) 
    
    def __str__(self):
        return f'Профиль пользователя {self.user.username}'
    
