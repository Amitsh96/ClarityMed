from random import random
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
from .forms import CreateUserForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate,login,logout
from .decorators import unauthenticated_user,allowed_users
from django.contrib.auth.models import User
from django.db.models import Count

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
    return render(request, 'doctor-dash\dashboarddoctor.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor_acc','admin']) 
def dashdoctorclient(request):
    return render(request, 'doctor-dash\dashdoctorclient.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor_acc','admin']) 
def dashdoctorequip(request):
    return render(request, 'doctor-dash\dashdoctorequip.html')

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
    return render(request, 'client-dash\dashclientappointment.html')

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
    return render(request, 'client-dash\dashclientparking.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['client_acc','admin']) 
def dashclientseker(request):
    return render(request, 'client-dash\dashclientseker.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['client_acc','admin']) 
def dashclienttreatment(request):
    return render(request, 'client-dash\dashclienttreatment.html')
#----------ENDCLIENT----------#

#----------RECEP----------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['recep_acc','admin']) 
def dashboardrecep(request):
    return render(request, 'recep-dash\dashboardrecep.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['recep_acc','admin']) 
def dashrecepclient(request):
    user_count = User.objects.filter(groups__name='client_acc').count()
    return render(request, 'recep-dash\dashrecepclient.html',{"user_count":user_count})

@login_required(login_url='login')
@allowed_users(allowed_roles=['recep_acc','admin']) 
def dashrecephelp(request):
    return render(request, 'recep-dash\dashrecephelp.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['recep_acc','admin']) 
def dashrecepinfo(request):
    return render(request, 'recep-dash\dashrecepinfo.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['recep_acc','admin']) 
def dashrecepreview(request):
    return render(request, 'recep-dash\dashrecepreview.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['recep_acc','admin']) 
def dashrecepsupply(request):
    return render(request, 'recep-dash\dashrecepsupply.html')
#----------ENDRECEP----------#