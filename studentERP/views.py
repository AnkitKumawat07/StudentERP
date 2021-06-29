from django.shortcuts import render
import random, time
from .settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib import messages
from loginadmin.models import loginadmin
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from librarymangement.models import librarybooks
from admin2_manage.models import studentdetail
from studentpanel.models import Challan,Semester

res2=None
email2=None

def otprequest(request):
    if request.method == 'POST':
        global email2
        email = request.POST['email']
        email2=email
        welcome = 'Welcome to ECB portal'
        global res2
        res = random.sample(range(0, 9), 6)
        msgmain = 'OTP to RESET PASSWORD is '
        recepient = []
        # getting data regarding admin_password and detail
        try:
            go = loginadmin.objects.get(admin_mail=email)
        except ObjectDoesNotExist:
            go = None
        msg = ''
        for i in range(len(res)):
            msg += str(res[i])
        res2=msg
        recepient.append(email)
        if len(email) < 4 or go is None:
            messages.error(request, 'Email Not found or not Registered ! ')
        else:
            send_mail(welcome, msgmain + msg, EMAIL_HOST_USER, recepient, fail_silently=False)
            return JsonResponse({'status': 'save'})
    else:
        return JsonResponse({'status': 'not_save'})


def index(request):
    # ------------------------------------------------------login admin ------------------------------------------------
    if request.method == 'POST' and 'adminloginbtn' in request.POST:
        enter_email = request.POST['admin_email']
        enter_pass = request.POST['admin_pass']
        # object of admin to match email and password
        admin_obj = loginadmin.objects.get(admin_mail=enter_email)
        if admin_obj.admin_mail == enter_email and admin_obj.admin_pword == enter_pass:
            return render(request, 'admin_manage.html')
        else:
            messages.error(request, 'Email Not found or not Registered ! ')

    # ---------------------------------------------Reset Password ------------------------------------------------------
    if request.method == 'POST' and 'changepass' in request.POST:
        enter_otp = request.POST['checkotp']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if enter_otp == res2 and pass1 == pass2:
            obj=loginadmin.objects.get(admin_mail=email2)
            obj.admin_pword=pass1
            obj.save()
            messages.error(request, 'Password is updated')
        else:
            messages.error(request, 'Password or otp is not matched ')

    #---------------------------------------------Library Login ________________________________________________________
    if request.method == 'POST' and 'Library_login' in request.POST:
        name=request.POST['lib_name']
        pass1=request.POST['lib_pass']
        try:
            admin_login=loginadmin.objects.get(admin_name=name)
        except ObjectDoesNotExist:
            admin_login=None
        if admin_login==None or admin_login.admin_pword!=pass1:
            messages.error(request,"Please Enter the right Entry")
        else:
            print(admin_login.admin_name,"---",admin_login.admin_pword,"--",admin_login.admin_panel)
            books = librarybooks.objects.all()
            return render(request,'library.html',{'books':books})

    #-------------------------------------------student Login-----------------------------------------------------------
    if request.method=='POST' and 'loginstudent' in request.POST:
        reg_id=request.POST['studentreg_id']
        pas = request.POST['studentpassword']
        try:
            student=studentdetail.objects.filter( student_id=reg_id).values()
        except ObjectDoesNotExist:
            student=None
        if student == None or pas !=student[0]['student_pass']:
            messages.error(request, "Please Enter the right Entry")
        else:
            print(student)
            try:
                semstudent=Semester.objects.filter(reg_id__student_id=reg_id).values()
            except ObjectDoesNotExist:
                semstudent=None
            try:
                challans=Challan.objects.filter(reg_id__student_id=reg_id).values()
            except ObjectDoesNotExist:
                challans=None
            print(challans)
            return render(request,'studentpanel.html',{'student':list(student),'semstudent':list(semstudent),'challans':list(challans)})
    return render(request, 'index.html')
