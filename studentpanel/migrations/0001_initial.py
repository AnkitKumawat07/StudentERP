# Generated by Django 3.0.7 on 2021-06-23 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin2_manage', '0004_studentdetail_student_gendere'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('sem_id', models.AutoField(primary_key=True, serialize=False)),
                ('sem1', models.CharField(default='00', max_length=2)),
                ('sem2', models.CharField(default='00', max_length=2)),
                ('sem3', models.CharField(default='00', max_length=2)),
                ('sem4', models.CharField(default='00', max_length=2)),
                ('sem5', models.CharField(default='00', max_length=2)),
                ('sem6', models.CharField(default='00', max_length=2)),
                ('sem7', models.CharField(default='00', max_length=2)),
                ('sem8', models.CharField(default='00', max_length=2)),
                ('reg_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin2_manage.studentdetail')),
            ],
        ),
        migrations.CreateModel(
            name='Challan',
            fields=[
                ('challan_id', models.AutoField(primary_key=True, serialize=False)),
                ('challan1', models.CharField(default='NONE', max_length=20)),
                ('challan2', models.CharField(default='NONE', max_length=20)),
                ('challan3', models.CharField(default='NONE', max_length=20)),
                ('challan4', models.CharField(default='NONE', max_length=20)),
                ('challan5', models.CharField(default='NONE', max_length=20)),
                ('challan6', models.CharField(default='NONE', max_length=20)),
                ('challan7', models.CharField(default='NONE', max_length=20)),
                ('challan8', models.CharField(default='NONE', max_length=20)),
                ('reg_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin2_manage.studentdetail')),
            ],
        ),
    ]
