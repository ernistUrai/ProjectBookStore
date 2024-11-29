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
    aut_books = models.ManyToManyField('books.Book', related_name='aut_books', blank=True)
    created_data = models.DateTimeField(auto_now_add=True)    
    
    def __str__(self):
        return self.name
    
    


class Book(models.Model):
    title = models.CharField('Китептин аталышы', max_length=100)
    author = models.CharField('Автор', max_length=100)
    price = models.DecimalField('Баасы', max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    publication_year = models.PositiveBigIntegerField('Басылган жылы')
    image = models.ImageField('Китептин сүрөтү', upload_to='books/')
    description = models.TextField('Китептин сүрөттөмөсү')
    isbn = models.CharField('ISBN', max_length=13, unique=True, null=True, blank=True)
    pages = models.PositiveIntegerField('Беттердин саны', default=0)
    stock = models.PositiveIntegerField('Саны', default=0)
    discount_price = models.DecimalField('Арзандатылган баа', max_digits=10, decimal_places=2, null=True, blank=True)
    
    @property
    def average_rating(self):
        ratings = self.comments.all().values_list('rating_book', flat=True)
        if ratings:
            return sum(int(r) for r in ratings) / len(ratings)
        return 0
    
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
    payment_status = models.CharField('Статус оплаты', max_length=100)  
    order_status = models.CharField('Статус заказа', max_length=100, choices=STATUS_CHOICES, default='new')     
    created_at = models.DateTimeField('Дата создания', auto_now_add=True) 
    
    
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
    
    
    
class FavoriteBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_data = models.DateTimeField('Дата создания', auto_now_add=True, null=True)
    
    class Meta:
        unique_together = ('user', 'book')
    
    def __str__(self):
        return f"{self.user.username} добавил книгу {self.book.title} в избранное"
    
