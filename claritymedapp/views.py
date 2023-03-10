from gettext import npgettext
from random import random
import datetime
from random import randrange
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages 
from claritymedapp.models import *
import mysql.connector
from django.http import JsonResponse
import random
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, SurveyForm , doc_app_form,client_add ,order_rec,order_doctor
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate,login,logout
from .decorators import unauthenticated_user,allowed_users
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User
from django.db.models import Count

from .models import survey,NavClass

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    database=" claritymed",
)
cursor = db_connection.cursor()
print(db_connection)

def index(request):
    return render(request, 'index.html')

@unauthenticated_user
def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:

        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('index')  #NEED TO CHECK PERMISSIONS
            else:
                messages.info(request, 'Username OR Password is incorrect')
            
        context={}
        return render(request, 'login.html',context)

@unauthenticated_user
def register(request):
   
    form=CreateUserForm()

    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, 'Account has been created for ' + username)

            group=Group.objects.get(name='client_acc')
            user.groups.add(group)
            
            return redirect('login')
    context={'form':form}
    return render(request, 'register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def buy(request):
    return render(request, 'buy.html')

@login_required(login_url='login')
def medicine(request):
    return render(request, 'medicine.html')
    
@login_required(login_url='login')
def about(request):
    return render(request, 'about.html')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')





#----------DOCTOR----------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor_acc','admin']) 
def dashboarddoctor(request):
    submitted = False
    if request.method == "POST":
        form = client_add(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('dashboarddoctor?submitted=True')
    else:
        form = client_add
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'doctor-dash\dashboarddoctor.html',{'form':form, 'submitted':submitted})

@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor_acc','admin']) 
def dashdoctorclient(request):
    user_count = clients1.objects.count()
    user_list=clients1.objects.all()


    submitted = False
    if request.method == "POST":
        form = doc_app_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('dashdoctorclient?submitted=True')
    else:
        form = doc_app_form
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'doctor-dash\dashdoctorclient.html', {'user_count':user_count,'user_list':user_list,'form':form,'submitted':submitted})

@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor_acc','admin']) 
def dashdoctorequip(request):
    supp=doc_eq.objects.all()
    submitted = False
    if request.method == "POST":
        form = order_doctor(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('dashdoctorequip?submitted=True')
    else:
        form = order_doctor
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'doctor-dash\dashdoctorequip.html',{"supp":supp,"form":form,'submitted':submitted})

@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor_acc','admin']) 
def dashdoctorequip_status(request):
    arr=random.choices(["???? ??????????","??????????"],k=8)
    return render(request, 'doctor-dash\dashdoctorequip_status.html',{'arr':arr})    

@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor_acc','admin']) 
def dashdoctorhelp(request):
    return render(request, 'doctor-dash\dashdoctorhelp.html')
#----------ENDDOCTOR----------#







#----------CLIENT----------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['client_acc','admin'])  
def dashboardclient(request):
    return render(request, 'client-dash\dashboardclient.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['client_acc','admin']) 
def dashclientappointment(request):
    user_list=User.objects.filter(groups__name='doctor_acc')
    submitted = False
    if request.method == "POST":
        form = doc_app_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('dashclientappointment?submitted=True')
    else:
        form = doc_app_form
        if 'submitted' in request.GET:
            submitted = True
   
    return render(request, 'client-dash\dashclientappointment.html',{'form':form, 'submitted':submitted,'user_list':user_list})
   

@login_required(login_url='login')
@allowed_users(allowed_roles=['client_acc','admin'])   
def dashclientinfo(request):
    return render(request, 'client-dash\dashclientinfo.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['client_acc','admin']) 
def dashclientonlinestore(request):
    return render(request, 'client-dash\dashclientonlinestore.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['client_acc','admin']) 
def dashclientparking(request):
    arr=random.choices(["????????","????????"],k=9)
    return render(request, 'client-dash\dashclientparking.html',{'arr':arr})

@login_required(login_url='login')
@allowed_users(allowed_roles=['client_acc','admin']) 
def dashclientseker(request):
    submitted = False
    if request.method == "POST":
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('dashclientseker?submitted=True')
    else:
        form = SurveyForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'client-dash\dashclientseker.html', {'form':form, 'submitted':submitted})

@login_required(login_url='login')
@allowed_users(allowed_roles=['client_acc','admin']) 
def dashclienttreatment(request):
    date=datetime.timedelta(minutes=randrange(120))
    return render(request, 'client-dash\dashclienttreatment.html',{'date':date})

@login_required(login_url='login')
@allowed_users(allowed_roles=['client_acc','admin']) 
def dashclientNAV(request):
    return render(request, 'client-dash\dashclientNAV.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['client_acc','admin']) 
def nav1(request):
    nav=NavClass.objects.filter(name_class='General')
    return render(request, 'navs/nav1.html',{'nav':nav})

@login_required(login_url='login')
@allowed_users(allowed_roles=['client_acc','admin']) 
def nav2(request):
    nav=NavClass.objects.filter(name_class='Neurology')
    return render(request, 'navs/nav2.html',{'nav':nav})

@login_required(login_url='login')
@allowed_users(allowed_roles=['client_acc','admin']) 
def nav3(request):
    nav=NavClass.objects.filter(name_class='Cardiology')
    return render(request, 'navs/nav3.html',{'nav':nav})

@login_required(login_url='login')
@allowed_users(allowed_roles=['client_acc','admin']) 
def nav4(request):
    nav=NavClass.objects.filter(name_class='Physiotherapy')
    return render(request, 'navs/nav4.html',{'nav':nav})
#----------ENDCLIENT----------#







#----------RECEP----------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['recep_acc','admin']) 
def dashboardrecep(request):
    submitted = False
    if request.method == "POST":
        form = client_add(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('dashboardrecep?submitted=True')
    else:
        form = client_add
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'recep-dash\dashboardrecep.html',{'form':form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['recep_acc','admin']) 
def dashrecepclient(request):

    user_count = clients1.objects.count()
    user_list=clients1.objects.all()

    submitted = False
    if request.method == "POST":
        form = doc_app_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('dashrecepclient?submitted=True')
    else:
        form = doc_app_form
        if 'submitted' in request.GET:
            submitted = True
   
    return render(request, 'recep-dash\dashrecepclient.html',{'user_count':user_count,'user_list':user_list,'form':form, 'submitted':submitted})

@login_required(login_url='login')
@allowed_users(allowed_roles=['recep_acc','admin']) 
def dashrecephelp(request):
    return render(request, 'recep-dash\dashrecephelp.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['recep_acc','admin']) 
def dashrecepreview(request):
    surv=survey.objects.all()
    return render(request, 'recep-dash\dashrecepreview.html',{'surv':surv})

@login_required(login_url='login')
@allowed_users(allowed_roles=['recep_acc','admin']) 
def dashrecepsupply(request):
    supp=recep_eq.objects.all()
    submitted = False
    if request.method == "POST":
        form = order_rec(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('dashrecepsupply?submitted=True')
    else:
        form = order_rec
        if 'submitted' in request.GET:
            submitted = True
   
    return render(request, 'recep-dash\dashrecepsupply.html',{"supp":supp,"form":form,'submitted':submitted})
#----------ENDRECEP----------#