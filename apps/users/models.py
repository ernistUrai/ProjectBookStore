from django.db import models
from django.contrib.auth.models import User
from apps.books.models import Book

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField('Телефон номери', max_length=15, blank=True)
    address = models.CharField('Дареги', max_length=255, blank=True)
    favorite_books = models.ManyToManyField(Book, related_name='favorited_by', blank=True)
    
    def __str__(self):
        return f'{self.user.username} профили'

class ReadingHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_read = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.book.title}'
