from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    path('semester',views.SemResult,name="SemResult"),
    path('challan',views.ChallanResult,name="challan"),
    path('studentupdate',views.StudentUpdate,name="StudentUpdate"),
]