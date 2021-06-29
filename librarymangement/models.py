from django.db import models
from admin2_manage.models import studentdetail
from datetime import date
from django.conf import settings
class librarybooks(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=255, null=False,unique=True)
    book_author = models.CharField(max_length=255, null=False)
    book_ava = models.IntegerField(null=False)

    def __str__(self):
        return self.book_name

class BooksToStudents(models.Model):
    bs_id=models.AutoField(primary_key=True)
    stud_id=models.ForeignKey(studentdetail,on_delete=models.CASCADE)
    books_id=models.ForeignKey(librarybooks,on_delete=models.CASCADE)
    date_issue=models.DateField(default=date.today)
    def __str__(self):
        return str(self.bs_id)