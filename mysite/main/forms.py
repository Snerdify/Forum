from django import forms
from .models import User
from django.forms import ModelForm


class RegisterForm(forms.ModelForm):
    
    username=forms.CharField(max_length=200)
    email=forms.EmailField()
    first_name=forms.CharField(max_length=200)
    last_name=forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username','email', 'first_name', 'last_name', 'password']


class LoginForm(forms.Form):
    username=forms.CharField(max_length=200)
    password=forms.CharField(max_length=200)
    email=forms.EmailField()
    class Meta:
        fields=['username','password']
