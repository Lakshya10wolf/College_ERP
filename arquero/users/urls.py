from django.urls import path, include

from . import views
from .views import index, areg, sreg, tp, stu_detail, admin_detail

app_name = 'users'
urlpatterns = [
    ##################################
    # --------------Home Page---------
    ##################################
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    ###################################
    # --------------Admin--------------
    ###################################

    path('areg', views.areg, name='areg'),
    path('alogin', views.alogin, name='alogin'),
    path('alogout', views.alogout, name='alogout'),
    path('apanel', views.apanel, name='apanel'),
    path('aprofile', admin_detail.ap, name='ap'),
    path('adminatt', admin_detail.a_att, name='a_att'),
    path('anew', admin_detail.anew, name='anew'),
    path('anot', admin_detail.anot, name='anot'),
    path('subselect', admin_detail.subselect, name='subselect'),
    path('aedit', admin_detail.aedit, name='aedit'),

    # --------------Admin Password--------
    path('apass/', include('django.contrib.auth.urls')),
    path('apass', views.apass, name='apass'),

    ####################################
    # --------------Student-------------
    ######################################

    path('sreg', views.sreg, name='sreg'),
    path('slogin', views.slogin, name='slogin'),
    path('spanel', stu_detail.spanel, name='spanel'),
    path('slogout', views.slogout, name='slogout'),
    path('stu_profile', stu_detail.sp, name='stu_profile'),
    path('satt', stu_detail.satt, name='satt'),
    path('spro', stu_detail.spro, name='spro'),
    path('sass', stu_detail.ass, name='ass'),

    # --------------Student Password--------
    path('spass/', include('django.contrib.auth.urls')),
    path('spass', stu_detail.spass, name='spass'),

    #######################################
    # ------------Teacher Panel-------------
    #######################################

    path('treg', views.treg, name='treg'),
    path('tlogin', views.tlogin, name='tlogin'),
    path('tpanel', views.tpanel, name='tpanel'),
    path('tlogout', views.tlogout, name='tlogout'),
    path('tea_profile', tp.tea_profile, name='tea_profile'),
    path('tatt', tp.tatt, name='tatt'),
    path('tstuatt', tp.tstuatt, name='tstuatt'),
    path('tpro', tp.tpro, name='tpro'),
    path('tass', tp.tass, name='tass'),
    ##path('tea_sub',views.tea_sub,name='tea_sub'),

    # --------------Student Password--------
    path('tpass/', include('django.contrib.auth.urls')),
    path('tpass', tp.tpass, name='tpass'),
    #######################################
    # -------------Notification-----------
    #######################################
    path('noti', views.noti, name='tnoti'),
    #######################################
    # -------------FEEDBACK-----------
    #######################################
    path('feedback', views.fedback, name='fedback'),

]
