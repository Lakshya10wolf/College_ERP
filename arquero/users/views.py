from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import viewsets

from .models import adm, stu, notify, teacher, feedback, Teacher_Attendance, sub, Student_Performance, \
    Student_Attendance, Assignment


######
######
# ---------------------Main Page--------------------
######
######

def index(request):
    # return render(request, 'index.html', {'name': 'amit'})
    if request.method == "POST":
        name = request.POST.get('tname')
        email = request.POST.get('email')
        message = request.POST.get('message')

        n = feedback(name=name, email=email, message=message)
        n.save()
        return redirect('/')


    else:
        return render(request, 'index.html')


######
######
# ---------------------Admin Portal-------------------
######
######

# ----------------------Admin registration-------------
def areg(request):
    if request.method == 'POST':
        clgname = request.POST.get('clgname')
        clgcode = request.POST.get('clgcode')
        uniname = request.POST.get('uniname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        pas1 = request.POST.get('pwd1')
        pas2 = request.POST.get('pwd2')
        if pas1 == pas2:
            if User.objects.filter(username=username).exists():
                messages.success(request, 'Username Already Taken')
                return render(request, 'admin_reg.html')
            else:
                user = User.objects.create_user(username=username, password=pas1, email=email)
                newuser = adm(clg_name=clgname, clg_code=clgcode, uni_name=uniname, user=user)
                newuser.save();
                return render(request, 'alogin.html')

        else:
            messages.info(request, 'password not working........')
            return render('admin_reg.html')
        return redirect('/')

    else:
        return render(request, 'admin_reg.html')


# --------------------Admin Login---------------
def alogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pas = request.POST.get('password')

        user = auth.authenticate(username=username, password=pas)

        if user is not None:
            auth.login(request, user)
            return redirect('/apanel')

        else:
            return redirect('/')

    return render(request, 'alogin.html')


# ------------------Admin Logout---------------------
def alogout(request):
    auth.logout(request)
    return redirect('/')


# ------------------Admin Panel----------------------
def apanel(request):
    return render(request, 'apanel.html')


# ------------------Admin Password-------------------
def apass(request):
    return render(request, 'adpass.html')


@login_required(login_url='/alogin/')
class admin_detail(viewsets.ModelViewSet):
    def ap(request):
        datas = adm.objects.filter(user=request.user)
        return render(request, 'admin_profile.html', {'data': datas})

    def a_att(request):
        if request.method == 'POST':
            tid = request.POST.get('tid')
            date = request.POST.get('date')
            att = request.POST.get('att')
            sin = request.POST.get('sin')
            sout = request.POST.get('sout')

            Teacher_Attendance.objects.create(Teacher_id=tid, date=date, Attendance=att, Sign_in=sin, Sign_out=sout)

            return render(request, 'adminatt.html')

        return render(request, 'adminatt.html')

    def anew(request):
        return render(request, 'abat.html')

    def anot(request):
        if request.method == 'POST':
            title = request.POST.get('title')
            comment = request.POST.get('comment')
            n = notify(title=title, notification=comment)
            return render(request, 'anot.html')

        else:
            return render(request, 'anot.html')

    def subselect(request):
        data = teacher.objects.all().order_by('name')

        if request.method == 'POST':
            subject1 = request.POST.get('sub')
            sem = request.POST.get('semester')
            course = request.POST.get('course')

            sub.objects.create(subject=subject1, sem=sem, course=course)

            return render(request, 'a_subselect.html', {'datas': data})

        else:
            return render(request, 'a_subselect.html')

    def aedit(request):
        return render(request, 'aedit.html')


########
########
# ---------------------Student Panel-----------------------
########
########

def sreg(request):
    if request.method == 'POST':
        clgname = request.POST.get('clgname')
        clgcode = request.POST.get('clgcode')
        uniname = request.POST.get('uniname')
        semester = request.POST.get('semester')
        coursename = request.POST.get('coursename')
        email = request.POST.get('email')
        name = request.POST.get('name')
        f_name = request.POST.get('fname')
        m_name = request.POST.get('mname')
        rno = request.POST.get('rno')
        dob = request.POST.get('dob')
        jy = request.POST.get('jy')
        username = request.POST.get('username')
        pas1 = request.POST.get('pwd1')
        pas2 = request.POST.get('pwd2')
        if pas1 == pas2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Taken')
                return render(request, 'admin_reg.html')
            else:
                user = User.objects.create_user(username=username, password=pas1, email=email)
                newuser1 = stu(clg_name=clgname, clg_code=clgcode, uni_name=uniname, semester=semester,
                               coursename=coursename, name=name, f_name=f_name, m_name=m_name, rno=rno, dob=dob, jy=jy,
                               user=user)
                newuser1.save()
                return redirect('/slogin')

        else:
            messages.info(request, 'password not working........')
            return render('student_reg.html')
        return redirect('/')

    else:
        return render(request, 'student_reg.html')


def slogin(request):
    if request.method == "POST":
        username1 = request.POST.get('username1')
        print(username1)
        password1 = request.POST.get('password1')

        user = auth.authenticate(username=username1, password=password1)

        if user is not None:
            auth.login(request, user)
            return redirect('/spanel')

        else:
            return redirect('/slogin')

    return render(request, 'slogin.html')


def slogout(request):
    auth.logout(request)
    return redirect('/')


@login_required(login_url='/slogin/')
class stu_detail(viewsets.ModelViewSet):
    def sp(request):
        datas = stu.objects.filter(user=request.user)
        return render(request, 'stu_profile.html', {'data': datas})

    def spanel(request):
        return render(request, 'spanel.html')

    def stu_profile(request):
        return render(request, 'stu_profile.html')

    def satt(request):
        da = Student_Attendance.objects.filter(Roll_no=request.user.username)
        return render(request, 'satt.html', {'data': da})

    def spass(request):
        return render(request, 'stu_pass.html')

    def spro(request):
        da = Student_Performance.objects.filter(Roll_no=request.user.username)

        return render(request, 'spro.html', {'data': da})

    def ass(request):
        da = Assignment.objects.all()
        return render(request, 'assgiver.html', {'data': da})


########
########
# ---------------------Teacher Panel-----------------------
########
########
def treg(request):
    if request.method == 'POST':
        clgname = request.POST.get('clgname')
        clgcode = request.POST.get('clgcode')
        uniname = request.POST.get('uniname')
        email = request.POST.get('email')
        name = request.POST.get('name')
        f_name = request.POST.get('fname')
        m_name = request.POST.get('mname')
        rno = request.POST.get('rno')
        dob = request.POST.get('dob')
        jy = request.POST.get('jy')
        username = request.POST.get('username')
        pas1 = request.POST.get('pwd1')
        pas2 = request.POST.get('pwd2')
        if pas1 == pas2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Taken')
                return render(request, 'teacher_reg.html')
            else:
                user = User.objects.create_user(username=username, password=pas1, email=email)
                newuser2 = teacher(clg_name=clgname, clg_code=clgcode, uni_name=uniname, name=name, f_name=f_name,
                                   m_name=m_name, rno=rno, dob=dob, jy=jy, user=user)
                newuser2.save();
                return redirect('/')

        else:
            messages.info(request, 'password not working........')
            return render('teacher_reg.html')
        return redirect('/')

    else:
        return render(request, 'teacher_reg.html')


def tlogin(request):
    if request.method == "POST":
        username2 = request.POST.get('username2')
        password2 = request.POST.get('password2')

        user = auth.authenticate(username=username2, password=password2)

        if user is not None:
            auth.login(request, user)
            return redirect('/tpanel')

        else:
            return redirect('/tlogin')

    return render(request, 'tlogin.html')


def tlogout(request):
    auth.logout(request)
    return redirect('/')


def tpanel(request):
    return render(request, 'tpanel.html')



@login_required(login_url='/tlogin/')
class tp(viewsets.ModelViewSet):

    def tea_profile(request):
        datas = teacher.objects.filter(user=request.user)
        return render(request, 'tea_profile.html', {'data': datas})

    def tatt(request):
        da = Teacher_Attendance.objects.filter(Teacher_id=request.user.username)
        return render(request, 'tatt.html', {'data': da})

    def tpass(request):
        return render(request, 'tpass.html')

    def tpro(request):
        da = sub.objects.all().order_by('subject')
        if request.method == 'POST':
            tid = request.POST.get('tid')
            subject1 = request.POST.get('sub')
            pap = request.POST.get('pap')
            mark = request.POST.get('mark')
            note = request.POST.get('note')

            Student_Performance.objects.create(Roll_no=tid, subject=subject1, Paper_name=pap, Marks=mark, Note=note)

            return render(request, 'tpro.html', {'data': da})

        return render(request, 'tpro.html', {'data': da})

    def tass(request):
        if request.method == 'POST':
            title = request.POST.get('title')
            desc = request.POST.get('desc')
            file = request.POST.get('pdffile')

            Assignment.objects.create(title=title, desc=desc, file=file)

        return render(request, 'tass.html')

    def tstuatt(request):
        da = sub.objects.all().order_by('subject')
        if request.method == 'POST':
            tid = request.POST.get('tid')
            subject1 = request.POST.get('sub')
            date = request.POST.get('date')
            att = request.POST.get('att')
            note = request.POST.get('note')

            Student_Attendance.objects.create(Roll_no=tid, subject=subject1, date=date, Attendance=att, Note=note)

            return render(request, 'tstuatt.html', {'data': da})

        return render(request, 'tstuatt.html', {'data': da})


##    datas = subject.objects.all()
##    return render(request, 'tea_sub.html', {'data': datas})

### --------------notification for all----------

def noti(request):
    noty = notify.objects.all()
    return render(request, 'noti.html', {'data': noty})


def fedback(request):
    fed = feedback.objects.all()
    return render(request, 'feedback.html', {'data': fed})
