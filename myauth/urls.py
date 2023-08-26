from django.urls import path
from .views import logining, logouting, profile, register

urlpatterns = [
    path('myauth/', logining, name='login'),
    path('mylog/', logouting, name='logout'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register')
]