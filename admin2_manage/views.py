from django.shortcuts import render
from django.http import JsonResponse
from .models import studentdetail, subjectDetails
from librarymangement.models import BooksToStudents
from studentpanel.models import Challan, Semester
from collections import defaultdict
def adminmain(request):
    return render(request, 'admin_manage.html')


def studentadddata(request):
    if request.method == "POST":
        name = request.POST['name']
        registration_id = request.POST['regid']
        Mobile = request.POST['mob']
        email = request.POST['email']
        pass1 = request.POST['pass']
        pass2 = request.POST['repass']
        dept = request.POST['dept']
        year = request.POST['year']
        print(name + registration_id + Mobile + email + pass1 + pass2 + dept + year)
        if (pass1 != pass2):
            return JsonResponse({'status': 'no_match'})
        elif (len(Mobile) != 10):
            return JsonResponse({'status': 'wrong_num'})
        elif (len(email) < 5):
            return JsonResponse({'status': 'not_email'})
        else:
            student = studentdetail(student_name=name, student_id=registration_id, student_mobile=Mobile,
                                    student_email=email, student_pass=pass1, student_dept=dept, student_year=year)
            student.save()
            return JsonResponse({'status': 'Save'})
    else:
        return JsonResponse({'status': 'not_save'})


def subjectadd(request):
    if request.method == "POST":
        sem = request.POST['sem']
        subj = request.POST['subj']
        text = request.POST['text']
        if len(sem) == 0 or len(subj) == 0 or len(text) == 0:
            return JsonResponse({'status': 'fill_all'})
        else:
            subject = subjectDetails(sem=sem, sub_id=subj, sub_detail=text)
            subject.save()
            return JsonResponse({'status': 'pass'})
    else:
        return JsonResponse({'status': 'not_pass'})

def getStudentData(request):
    dic=defaultdict(list)
    if request.method =="POST":
        reg_id=request.POST['reg_id']
        try:
            student_data=studentdetail.objects.filter(student_id=reg_id).values()
        except ObjectDoesNotExist:
            student_data=None
        if student_data == None or len(student_data)==0:
            return JsonResponse({'status':'wrong_no'})
        else:
            print(list(student_data))
            check = BooksToStudents.objects.filter(stud_id__student_id=reg_id)
            for ch in check:
                dic[ch.bs_id] = [ch.books_id.book_name, ch.date_issue]
            try:
                challanstudent = Challan.objects.filter(reg_id__student_id=reg_id).values()
            except ObjectDoesNotExist:
                challanstudent = None
            try:
                semstudent = Semester.objects.filter(reg_id__student_id=reg_id).values()
            except ObjectDoesNotExist:
                semstudent = None
            print(challanstudent)
            return JsonResponse({'status':'pass','student_data':list(student_data),'booksdata':dic,'semstudent': list(semstudent),'challanstudent':list(challanstudent)})
    else:
        return JsonResponse({'status':'no_pass'})
