from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from .models import librarybooks, BooksToStudents
from django.db.utils import IntegrityError
from admin2_manage.models import studentdetail
from django.core.exceptions import ObjectDoesNotExist
from collections import defaultdict
def librarymain(request):
    books = librarybooks.objects.all()
    print("yessss")
    print(books)
    return render(request, 'library.html', {'books': books})


def addBooks(request):
    if request.method == "POST":
        book_id = request.POST.get('book_id')
        book_name = request.POST['book_name']
        book_author = request.POST['book_author']
        no_books = request.POST['no_books']
        if no_books == 0 or len(book_name) == 0 or len(book_author) == 0:
            return JsonResponse({'status': 'wrong'})
        try:
            if (book_id == ''):
                book = librarybooks(book_name=book_name, book_author=book_author, book_ava=no_books)
            else:
                book = librarybooks(book_id=book_id, book_name=book_name, book_author=book_author, book_ava=no_books)
            book.save()
        except IntegrityError:
            return JsonResponse({'status': 'exist'})
        all_book = librarybooks.objects.values()
        book_data = list(all_book)
    return JsonResponse({'status': 'save', 'book_data': book_data})


def delete_book(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        book_id = librarybooks.objects.get(book_id=id)
        book_id.delete()
        return JsonResponse({'status': 'done'})
    else:
        return JsonResponse({'status': 'undone'})


def edit_book(request):
    id = "17EEBCS010"
    ans = studentdetail.objects.get(student_id=id)
    check = BooksToStudents.objects.filter(stud_id__student_id='17EEBCS010')
    print(check)
    for ch in check:
        print(ch.books_id)
    if request.method == "POST":
        id = request.POST.get('sid')
        print(id)
        book_id = librarybooks.objects.get(book_id=id)
        book_data = {"id": book_id.book_id, "name": book_id.book_name, "author": book_id.book_author,
                     "number": book_id.book_ava}
        return JsonResponse({'status': 'done', 'book_data': book_data})
    else:
        return JsonResponse({'status': 'undone'})


def booktostudent(request):
    dic = defaultdict(list)
    if request.method == "POST":
        bk_id = request.POST['book_id']
        date = request.POST['date']
        sd_id = request.POST['stud_id']
        stud_id = studentdetail.objects.get(student_id=sd_id)
        book_id = librarybooks.objects.get(book_name=bk_id)
        obj = BooksToStudents(stud_id=stud_id, books_id=book_id, date_issue=date)
        obj.save()
        check = BooksToStudents.objects.filter(stud_id__student_id=stud_id)
        for ch in check:
            dic[ch.bs_id] = [ch.books_id.book_name, ch.date_issue]
        return JsonResponse({'status': 'save','booksdata':dic})
    else:
        return JsonResponse({'satus': 'not_save'})


def studentbookdata(request):
    dic=defaultdict(list)
    if request.method=="POST":
        reg_id=request.POST['reg_id']
        try:
            student=studentdetail.objects.filter(student_id=reg_id).values()
        except ObjectDoesNotExist:
            student=None
        if student==None or len(student)==0:
            return  JsonResponse({'status':'not_exist'})
        else:
            check = BooksToStudents.objects.filter(stud_id__student_id=reg_id)
            for ch in check:
                dic[ch.bs_id]=[ch.books_id.book_name,ch.date_issue]
            return JsonResponse({'status':'save','student':list(student),'bookstostudent':dic})
    else:
        return JsonResponse({'status':'not_save'})

def deletestudentbook(request):
    if request.method=="POST":
        bs_id=request.POST['id']
        print(bs_id)
        object=BooksToStudents.objects.get(bs_id=bs_id)
        object.delete()
        return JsonResponse({'status':'save'})
    else:
        return JsonResponse({'status':'not_save'})