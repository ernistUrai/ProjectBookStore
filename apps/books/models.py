from django.db import models
from django.contrib.auth.models import User

# Create your models here.


 
class Category(models.Model):
    name = models.CharField('Название категории', max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Author(models.Model):
    name = models.CharField('Имя автора', max_length=100)
    year_birth = models.PositiveSmallIntegerField('Год рождения')
    life_story = models.TextField('Краткая биография')
    aut_image = models.ImageField('Фотография автора')
    created_data = models.DateTimeField(auto_now_add=True)    
    
    def __str__(self):
        return self.name
    
    


class Book(models.Model):
    title = models.CharField('Названия книги', max_length=100)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE, verbose_name='Автор')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    publication_year = models.PositiveBigIntegerField('Год издания')
    image = models.ImageField('Китептин сүрөтү', upload_to='books/')
    description = models.TextField('Китептин сүрөттөмөсү')
    isbn = models.CharField('ISBN', max_length=13, unique=True, null=True, blank=True)
    
    @property
    def average_rating(self):
        ratings = self.coments.all().values_list('rating_book', flat=True)
        if ratings:
            return sum(int(r) for r in ratings) / len(ratings)
        return 0
    
    def __str__(self):
        return self.title
    
    


    
class ComentBook(models.Model):
    RATING_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    
    book = models.ForeignKey(Book,  related_name='coments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coment = models.TextField('Комментарий')
    rating_book = models.CharField('Рейтинг книги', max_length=25, choices=RATING_CHOICES, default="1")
    created_data = models.DateTimeField('Дата создания', auto_now_add=True, null=True)
    
    def __str__(self): 
        return f'Комментарий к книге {self.book.title} от {self.user.username}'
    
    
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_data = models.DateTimeField('Дата создания', auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Количество', default=1)
    
    def __str__(self):
        return f'{self.quantity} {self.book.title} {self.cart} '


class Order(models.Model):
    STATUS_CHOICES = (
        ('С картой', 'С картой'),
        ('Наличными', 'Наличными'),
        )           
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    total_price = models.DecimalField('Сумма заказа', max_digits=10, decimal_places=2)    
    delivery_address = models.CharField('Адрес доставки', max_length=100)       
    payment_status = models.CharField('Статус оплаты', max_length=50, choices=STATUS_CHOICES)  
    created_at = models.DateTimeField('Дата создания', auto_now_add=True) 

    def __str__(self):
        return f'Заказ от {self.user.username}'