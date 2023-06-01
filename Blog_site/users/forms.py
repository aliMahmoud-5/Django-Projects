from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from users.models import profile


class user_register(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class updateinfo(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email','username']

class updatepic(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['pic']