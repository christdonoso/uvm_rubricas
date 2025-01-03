from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.decorators.http import require_POST

from .models import Usuario, Estudiante

from utilities import tools
# Create your views here.


def index(request):
    return redirect('login')


def home(request):
    usuario = Usuario.get_usuario(request)
    return render(request, 'home.html', {'usuario':usuario})


def profile(request):
    usuario = Usuario.get_usuario(request)
    print(usuario.profile_image)
    return render(request, 'profile.html', {'usuario':usuario})


def update_profile(request):
    usuario = Usuario.get_usuario(request)
    if request.FILES:
        usuario.profile_image = request.FILES['profile_image']
        usuario.names = request.POST['names']
        usuario.last_names = request.POST['last_names']
        usuario.email = request.POST['email']
        usuario.save()
    else:
        usuario.names = request.POST['names']
        usuario.last_names = request.POST['last_names']
        usuario.email = request.POST['email']
        usuario.save()

    messages.add_message(request, messages.SUCCESS, 'Informacion actualizada con exito')
    return redirect('profile')
    """
    def update_profile(request):
        usuario = Usuario.get_usuario(request)
        if request.FILES:
            usuario.profile_image = request.FILES.get('profile_image')
        
        # Actualiza los campos comunes
        for field in ['names', 'last_names', 'email']:
            setattr(usuario, field, request.POST.get(field, getattr(usuario, field)))
        
        usuario.save()
        messages.success(request, 'Información actualizada con éxito')
        return redirect('profile')
    """


def add_student(request):
    usuario = Usuario.get_usuario(request)
    if request.method == 'GET':
        return render(request, 'add_student.html',{'usuario':usuario})
    else:
        cleaned_data = tools.remove_csrftoken(request.POST)
        Estudiante.objects.create(**cleaned_data)
        messages.add_message(request, messages.SUCCESS, 'Estudiante creado con exito')
        return render(request, 'add_student.html',{'usuario':usuario})
        

def students_list(request):
    usuario = Usuario.get_usuario(request)
    estudiantes = Estudiante.objects.all()
    return render(request, 'students_list.html', {'usuario':usuario, 'estudiantes':estudiantes})


def edit_student(request):
    estudiante = Estudiante.objects.get(id = request.GET['id'])
    if request.method == 'GET':
        return render(request, 'edit_student.html',{'estudiante':estudiante})
    else:
        cleaned_data = tools.remove_csrftoken(request.POST)
        tools.update_model_object(estudiante,cleaned_data)
        messages.add_message(request, messages.SUCCESS, 'Estudiante editado con exito')
        return render(request, 'edit_student.html',{'estudiante':estudiante})


@require_POST
def delete_student(request):
    estudiante = Estudiante.objects.get(id = request.POST['id'])
    estudiante.delete()
    messages.add_message(request, messages.SUCCESS, f'Informacion de {estudiante.run } eliminada con exito')
    return redirect('students_list')