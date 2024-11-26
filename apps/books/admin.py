from django.contrib import admin
from .models import Category, Book, Order, ComentBook, Author

# Register your models here.
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Order)
admin.site.register(ComentBook)
admin.site.register(Author)

