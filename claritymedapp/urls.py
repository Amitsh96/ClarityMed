from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('index', views.index, name="index"),
    path('login', views.LoginPage, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('buy', views.buy, name="buy"),
    path('medicine', views.medicine, name="medicine"),
    path('about', views.about, name="about"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('register', views.register, name="register"),



    
    path('dashboardrecep', views.dashboardrecep, name="dashboardrecep"),


    #----------CLIENT----------#
    path('dashboardclient', views.dashboardclient, name="dashboardclient"),
    path('dashclientappointment', views.dashclientappointment, name="dashclientappointment"),
    path('dashclientinfo', views.dashclientinfo, name="dashclientinfo"),
    path('dashclientonlinestore', views.dashclientonlinestore, name="dashclientonlinestore"),
    path('dashclientparking', views.dashclientparking, name="dashclientparking"),
    path('dashclientseker', views.dashclientseker, name="dashclientseker"),
    path('dashclienttreatment', views.dashclienttreatment, name="dashclienttreatment"),
    path('dashclientNAV', views.dashclientNAV, name="dashclientNAV"),
    path('nav1', views.nav1, name="nav1"),
    path('nav2', views.nav2, name="nav2"),
    path('nav3', views.nav3, name="nav3"),
    path('nav4', views.nav4, name="nav4"),
    #----------ENDCLIENT----------#

    #----------DOCTOR----------#
    path('dashboarddoctor', views.dashboarddoctor, name="dashboarddoctor"),
    path('dashdoctorclient', views.dashdoctorclient, name="dashdoctorclient"),
    path('dashdoctorequip', views.dashdoctorequip, name="dashdoctorequip"),
    path('dashdoctorhelp', views.dashdoctorhelp, name="dashdoctorhelp"),
    #----------ENDDOCTOR----------#

    #----------RECEP----------#
    path('dashboardrecep', views.dashboardrecep, name="dashboardrecep"),
    path('dashrecepinfo', views.dashrecepinfo, name="dashrecepinfo"),
    path('dashrecepclient', views.dashrecepclient, name="dashrecepclient"),
    path('dashrecephelp', views.dashrecephelp, name="dashrecephelp"),
    path('dashrecepreview', views.dashrecepreview, name="dashrecepreview"),
    path('dashrecepsupply', views.dashrecepsupply, name="dashrecepsupply"),
    #----------ENDRECEP----------#
]