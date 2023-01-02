from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import survey,doc_app
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2','first_name','last_name']

class SurveyForm(ModelForm):
    class Meta:
        model=survey
        fields=('cleaning', 'security', 'treatment', 'facilities', 'food')

class doc_app_form(ModelForm):
    class Meta:
        model=doc_app
        fields=('doc_id', 'doc_name', 'client_id', 'client_name', 'date_app')

