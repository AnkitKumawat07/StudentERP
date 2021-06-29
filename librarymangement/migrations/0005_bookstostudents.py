# Generated by Django 3.0.7 on 2021-06-16 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin2_manage', '0003_auto_20210606_0928'),
        ('librarymangement', '0004_auto_20210614_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='BooksToStudents',
            fields=[
                ('bs_id', models.AutoField(primary_key=True, serialize=False)),
                ('stud_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin2_manage.studentdetail')),
            ],
        ),
    ]
