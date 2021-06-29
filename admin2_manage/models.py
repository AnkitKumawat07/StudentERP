from django.db import models


# Create your models here.
class studentdetail(models.Model):
    student_no = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=30, null=False)
    student_id = models.CharField(max_length=30, null=False)
    student_gendere=models.CharField(max_length=10,default='MALE')
    student_mobile = models.CharField(max_length=10, null=False)
    student_email = models.EmailField(null=False)
    student_pass = models.CharField(max_length=30, null=False)
    student_dept = models.CharField(max_length=80, null=False)
    student_year=models.IntegerField(default=1998)
    def __str__(self):
        return self.student_id


class subjectDetails(models.Model):
    subject_no = models.AutoField(primary_key=True)
    sem = models.CharField(max_length=2, null=False)
    sub_id = models.CharField(max_length=250, null=False)
    sub_detail = models.TextField(null=False)

    def __str__(self):
        return "Sem - "+self.sem + "|| Subject - " + self.sub_id
