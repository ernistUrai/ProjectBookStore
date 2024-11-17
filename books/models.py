from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField('Название категории', max_length=100)
    
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField('Название книги', max_length=100)
    author = models.CharField('Автор', max_length=100)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publication_year = models.PositiveBigIntegerField('Год публикации книги')
    image = models.ImageField('Фотография книги' )
    description = models.TextField('Описание книги')
    
    def __str__(self):
        return self.title
    
    
