from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logining(request):
    redirect_url = reverse('profile')
    if request.user.is_authenticated:
        return redirect(redirect_url)
    if request.method == "GET":
        return render(request, 'myauth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(reverse('main'))
    return render(request, 'myauth/login.html', {'error':'user does not exist'})

def logouting(request):
    redirect_to = reverse('login')
    logout(request)
    return redirect(redirect_to)

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'myauth/register.html', {'form': form})
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            authenticate(username=username, password=password)
            # login(request, user)
            return redirect(reverse('login'))
        
    else:
        form = UserCreationForm()
    return render(request, 'myauth/register.html', {'form': form})

def profile(request):
    return render(request, 'myauth/profile.html')