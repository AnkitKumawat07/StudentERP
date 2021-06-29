from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from admin2_manage.models import studentdetail
from .models import Challan, Semester


def SemResult(request):
    if request.method == "POST":
        sem_id = request.POST.get('sem_id')
        sem1 = request.POST['sem1']
        sem2 = request.POST['sem2']
        sem3 = request.POST['sem3']
        sem4 = request.POST['sem4']
        sem5 = request.POST['sem5']
        sem6 = request.POST['sem6']
        sem7 = request.POST['sem7']
        sem8 = request.POST['sem8']
        reg = request.POST['reg_id']
        try:
            student = studentdetail.objects.get(student_id=reg)
        except ObjectDoesNotExist:
            student = None
        if student == None:
            return JsonResponse({'status': 'student_doesnot_exist'})
        if sem_id == '':
            object = Semester(sem1=sem1, sem2=sem2, sem3=sem3, sem4=sem4, sem5=sem5, sem6=sem6, sem7=sem7, sem8=sem8,
                              reg_id=student)
        else:
            object = Semester(sem_id=sem_id, sem1=sem1, sem2=sem2, sem3=sem3, sem4=sem4, sem5=sem5, sem6=sem6,
                              sem7=sem7, sem8=sem8,
                              reg_id=student)
        object.save()
        try:
            semstudent = Semester.objects.filter(reg_id__student_id=reg).values()
        except ObjectDoesNotExist:
            semstudent = None
        return JsonResponse({'status': 'save', 'semstudent': list(semstudent)})
    else:
        return JsonResponse({'status': 'not_save'})


def ChallanResult(request):
    if request.method == "POST":
        ch_id = request.POST['ch_id']
        ch1 = request.POST['ch1']
        challan2 = request.POST['challan2']
        challan3 = request.POST['challan3']
        challan4 = request.POST['challan4']
        challan5 = request.POST['challan5']
        challan6 = request.POST['challan6']
        challan7 = request.POST['challan7']
        challan8 = request.POST['challan8']
        reg = request.POST['reg_id']
        try:
            student = studentdetail.objects.get(student_id=reg)
        except ObjectDoesNotExist:
            student = None
        if student == None:
            return JsonResponse({'status': 'student_doesnot_exist'})
        if ch_id=='':
            challan = Challan(ch1=ch1, ch2=challan2, ch3=challan3, ch4=challan4, ch5=challan5,ch6=challan6, ch7=challan7, ch8=challan8, reg_id=student)
        else:
            challan = Challan(challan_id=ch_id,ch1=ch1, ch2=challan2, ch3=challan3, ch4=challan4, ch5=challan5, ch6=challan6,
                              ch7=challan7, ch8=challan8, reg_id=student)
        challan.save()
        try:
            challanstudent=Challan.objects.filter(reg_id__student_id=reg).values()
        except ObjectDoesNotExist:
            challanstudent=None
        return JsonResponse({'status': 'save','challanstudent':list(challanstudent)})
    else:
        return JsonResponse({'status': 'not_save'})

def StudentUpdate(request):
    stud_no=request.POST['stud_no']
    name=request.POST['name']
    regid=request.POST['regi']
    gender=request.POST['gender']
    mobile=request.POST['mobile']
    email=request.POST['email']
    pass1=request.POST['pass']
    pass2=request.POST['pass2']
    branch=request.POST['branch']
    year=request.POST['year']
    if pass1!=pass2:
        return JsonResponse({'status':'no_pass'})
    student=studentdetail(student_no=stud_no,student_name=name,student_id=regid,student_gendere=gender,student_mobile=mobile,student_email=email,student_pass=pass1,student_dept=branch,student_year=year)
    student.save()
    return  JsonResponse({'status':'save'})
