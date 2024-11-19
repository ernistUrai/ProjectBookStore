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
    
    

class Order(models.Model):
    STATUS_CHOICES = (
        ('new', 'Новый'),
        ('in_progress', 'В процессе'),
        ('done', 'Готов'),
        ('canceled', 'Отменен'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)        
    books = models.ManyToManyField('books.Book')       
    total_price = models.DecimalField('Сумма заказа', max_digits=10, decimal_places=2)      
    delivery_address = models.CharField('Адрес доставки', max_length=100)       
    paiment_status = models.CharField('Статус оплаты', max_length=100, default="new")      
    order_status = models.CharField('Статус заказа', max_length=100, choices=STATUS_CHOICES, default="new")     
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)       
    
    def __str__(self):
        return f'Заказ от {self.user.username}'
    