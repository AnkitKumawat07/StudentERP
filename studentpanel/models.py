from django.db import models
from admin2_manage.models import studentdetail


class Semester(models.Model):
    sem_id = models.AutoField(primary_key=True)
    sem1 = models.CharField(max_length=2, default='00')
    sem2 = models.CharField(max_length=2, default='00')
    sem3 = models.CharField(max_length=2, default='00')
    sem4 = models.CharField(max_length=2, default='00')
    sem5 = models.CharField(max_length=2, default='00')
    sem6 = models.CharField(max_length=2, default='00')
    sem7 = models.CharField(max_length=2, default='00')
    sem8 = models.CharField(max_length=2, default='00')
    reg_id = models.ForeignKey(studentdetail, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.sem_id)


class Challan(models.Model):
    challan_id = models.AutoField(primary_key=True)
    ch1 = models.CharField(max_length=20, default='00')
    ch2 = models.CharField(max_length=20, default='00')
    ch3 = models.CharField(max_length=20, default='00')
    ch4 = models.CharField(max_length=20, default='00')
    ch5 = models.CharField(max_length=20, default='00')
    ch6 = models.CharField(max_length=20, default='00')
    ch7 = models.CharField(max_length=20, default='00')
    ch8 = models.CharField(max_length=20, default='00')
    reg_id = models.ForeignKey(studentdetail, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.challan_id)
