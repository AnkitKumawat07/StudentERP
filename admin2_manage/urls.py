from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('',views.adminmain,name="adminmain"),
    path('/studentdata',views.studentadddata,name="studentadddata"),
    path('/addsubject',views.subjectadd,name="subjectadd"),
    path('studentData',views.getStudentData,name="getStudentData"),
]