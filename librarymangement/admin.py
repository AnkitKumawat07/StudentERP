from django.contrib import admin
from .models import librarybooks,BooksToStudents

# Register your models here.
admin.site.register(librarybooks)
admin.site.register(BooksToStudents)