from django import forms
from django.db import models
from django.forms import fields
from .models import Record
from datetime import date
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']
        widgets = {
            'username':forms.TextInput(attrs={'placeholder':'Akshay123'})
        }

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['name', 'date', 'amount', 'reason', 'status']
        widgets = {
            'date':forms.DateInput(attrs={'type':'date','value':date.today()})
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput())
    password = forms.CharField(label=_('Password'), strip=False,widget=forms.PasswordInput())