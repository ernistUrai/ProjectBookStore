# Generated by Django 5.1.3 on 2024-12-02 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0017_alter_book_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='aut_books',
        ),
    ]
