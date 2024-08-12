from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib import admin
from datetime import datetime
from django.utils import timezone


# Create your models here.


class adm(models.Model):
    clg_name = models.CharField(max_length=36)
    clg_code = models.IntegerField()
    uni_name = models.CharField(max_length=36)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # cover = models.ImageField(upload_to='covers/',blank=True)
    def __str__(self):
        return self.clg_name


class stu(models.Model):
    clg_name = models.CharField(max_length=36)
    clg_code = models.IntegerField()
    uni_name = models.CharField(max_length=36)
    semester = models.CharField(max_length=36)
    coursename = models.CharField(max_length=36)
    name = models.CharField(max_length=36)
    f_name = models.CharField(max_length=36)
    m_name = models.CharField(max_length=36)
    rno = models.CharField(max_length=36)
    dob = models.DateField()
    jy = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # cover = models.ImageField(upload_to='covers/',blank=True)
    def __str__(self):
        return self.rno


class notify(models.Model):
    title = models.CharField(max_length=30)
    notification = models.TextField(max_length=100)

    def __str__(self):
        return self.title


class teacher(models.Model):
    clg_name = models.CharField(max_length=36)
    clg_code = models.IntegerField()
    uni_name = models.CharField(max_length=36)
    name = models.CharField(max_length=36)
    f_name = models.CharField(max_length=36)
    m_name = models.CharField(max_length=36)
    rno = models.CharField(max_length=36)
    dob = models.DateField()
    jy = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.rno


class feedback(models.Model):
    name = models.CharField(max_length=36)
    email = models.EmailField()
    message = models.TextField(max_length=150)

    def __str__(self):
        return self.name


CATEGORIES = (
    ('A', 'Absent'),
    ('P', 'Present'),
)


class Teacher_Attendance(models.Model):
    Teacher_id = models.IntegerField()
    date = models.DateField('Date', default=timezone.now)
    Attendance = models.CharField(max_length=2, choices=CATEGORIES)
    Sign_in = models.TimeField(auto_now=False, auto_now_add=False, default=datetime.now())
    Sign_out = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return "{0} Attendace on {1}".format(self.Teacher_id, self.date)


class sub(models.Model):
    subject = models.CharField(max_length=36)
    sem = models.CharField(max_length=12)
    course = models.CharField(max_length=20)

    def __str__(self):
        return self.subject


class Assignment(models.Model):
    title = models.CharField(max_length=30)
    file = models.FileField()
    desc = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class Student_Attendance(models.Model):
    Roll_no = models.IntegerField()
    date = models.DateField('Date', default=timezone.now)
    subject = models.CharField(max_length=30)
    Attendance = models.CharField(max_length=10)
    Note = models.TextField(max_length=200, null=True)

    def __str__(self):
        return "{0} Attendace on {1}".format(self.Roll_no, self.date)


CATEGORIE = (
    ('PUT', 'PUT'),
    ('UT1', 'unit Test 1'),
    ('UT2', 'unit Test 2'),
)


class Student_Performance(models.Model):
    Roll_no = models.IntegerField()
    Paper_name = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    Marks = models.IntegerField()
    Note = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "{0} marks on {1} was {2} in {3}".format(self.Roll_no,self.subject, self.Marks, self.Paper_name)
