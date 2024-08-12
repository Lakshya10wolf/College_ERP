from django.urls import path

from . import views


app_name = 'stu'
urlpatterns = [
path('stureg',views.stureg,name='stureg')
]