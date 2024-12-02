# Generated by Django 5.1.3 on 2024-12-02 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_alter_book_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='discount_price',
        ),
        migrations.RemoveField(
            model_name='book',
            name='pages',
        ),
        migrations.RemoveField(
            model_name='book',
            name='stock',
        ),
        migrations.AlterField(
            model_name='author',
            name='aut_books',
            field=models.ManyToManyField(related_name='aut_books', to='books.book'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_year',
            field=models.PositiveBigIntegerField(verbose_name='Год издания'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Названия книги'),
        ),
    ]