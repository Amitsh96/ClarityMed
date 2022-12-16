from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import survey

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class SurveyForm(ModelForm):
    class Meta:
        model=survey
        fields=('cleaning', 'security', 'treatment', 'facilities', 'food')