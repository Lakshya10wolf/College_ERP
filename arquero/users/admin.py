from django.contrib import admin
from .models import adm, stu, notify, teacher, feedback, Teacher_Attendance, Student_Attendance, \
     sub, Student_Performance, Assignment

admin.site.register(adm)
admin.site.register(stu)
admin.site.register(notify)
admin.site.register(teacher)
admin.site.register(feedback)
admin.site.register(Teacher_Attendance)
admin.site.register(Student_Attendance)
admin.site.register(sub)
admin.site.register(Student_Performance)
admin.site.register(Assignment)
