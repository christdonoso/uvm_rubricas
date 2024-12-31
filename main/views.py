from django.shortcuts import render,redirect
from urllib import request
 

# Create your views here.


def index(request):
    return redirect('login')


def home(request):
    return render(request, 'home.html')


def profile(request):
    return render(request, 'profile.html')

