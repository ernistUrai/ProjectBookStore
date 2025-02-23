# Generated by Django 5.1.3 on 2024-11-21 17:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_comentbook_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='discount_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Арзандатылган баа'),
        ),
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, max_length=13, null=True, unique=True, verbose_name='ISBN'),
        ),
        migrations.AddField(
            model_name='book',
            name='pages',
            field=models.PositiveIntegerField(default=0, verbose_name='Беттердин саны'),
        ),
        migrations.AddField(
            model_name='book',
            name='stock',
            field=models.PositiveIntegerField(default=0, verbose_name='Саны'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(verbose_name='Китептин сүрөттөмөсү'),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='books/', verbose_name='Китептин сүрөтү'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Баасы'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_year',
            field=models.PositiveBigIntegerField(verbose_name='Басылган жылы'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Китептин аталышы'),
        ),
    ]
