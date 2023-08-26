from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=25, widget=forms.TextInput(attrs = {'class': 'form-control-lg'}))
    password = forms.CharField(max_length=35, widget=forms.PasswordInput(attrs = {'class': 'form-control-lg'}))

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# class RegisterForm(forms.Form):
#     username = forms.CharField(max_length=25, widget=forms.TextInput(attrs = {'class': 'form-control-lg'}))
#     password = forms.CharField(max_length=35, widget=forms.PasswordInput(attrs = {'class': 'form-control-lg'}))
#     # email = forms.EmailField(widget=forms.TextInput(attrs = {'class': 'form-control-lg'}))