from django.shortcuts import render,redirect
 

# Create your views here.


def index(request):
    return redirect('login')


def home(request):
    return render(request, 'home.html')