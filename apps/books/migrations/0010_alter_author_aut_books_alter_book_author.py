# Generated by Django 5.1.3 on 2024-11-26 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_merge_20241126_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='aut_books',
            field=models.ManyToManyField(blank=True, related_name='aut_books', to='books.book'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100, verbose_name='Автор'),
        ),
    ]
