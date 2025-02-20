from django.shortcuts import render
from .models import CasoCLinicoConocido

# Create your views here.


def edit_casoclinicoconocido(request):
    if request.method == 'GET':
        
        return render(request, 'edit_casoclinicoconocido.html')
    else:
        print(request.POST)
        return render(request, 'edit_casoclinicoconocido.html')
