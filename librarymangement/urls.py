from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls import url
urlpatterns=[
    path('',views.librarymain,name="librarymain"),
    path('/Books',views.addBooks,name="addBooks"),
    path('/delete',views.delete_book,name="delete"),
    path('edit',views.edit_book,name="edit"),
    path('bookstostudent',views.booktostudent,name="booktostudent"),
    path('studentbookdata',views.studentbookdata,name="studentbookdata"),
    path('deletestudentbook',views.deletestudentbook,name="deletestudentbook"),
]