# Generated by Django 3.0.7 on 2021-06-14 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarymangement', '0002_auto_20210613_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librarybooks',
            name='book_author',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='librarybooks',
            name='book_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
