

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from item.models import item


class register(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

        username = forms.CharField(widget = forms.TextInput(attrs ={ 'placeholder':'username'}))
        email = forms.EmailField(widget = forms.PasswordInput(attrs ={ 'placeholder':'email'}))
        password1 = forms.CharField(widget = forms.PasswordInput(attrs ={ 'placeholder':'password'}))
        password2 = forms.CharField(widget = forms.PasswordInput(attrs ={ 'placeholder':'re-enter password'}))
        
class loginform(AuthenticationForm):
    
    class Meta:
        model = User
        fields = ('username','password1')

        username = forms.CharField(widget = forms.TextInput(attrs ={ 'placeholder':'username'}))
        password1 = forms.CharField(widget = forms.PasswordInput(attrs ={ 'placeholder':'password'}))

