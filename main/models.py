from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    names = models.CharField(max_length=50)
    last_names = models.CharField(max_length=50)
    profile_image = models.ImageField(null=True, blank=True, upload_to='images/')
    personal_info = models.TextField()
    email = models.EmailField(max_length=50)
 
    def __str__(self):
        return self.names + ' ' + self.last_names
    
    @staticmethod
    def get_usuario(request):
        user = request.user
        usuario = Usuario.objects.get(user = user)
        return usuario

    @staticmethod
    def filter_usuario(request):
        user = request.user
        usuario = Usuario.objects.filter(user = user)
        return usuario
    

class Estudiante(models.Model):
    run = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    names = models.CharField(max_length=50)
    surenames = models.CharField(max_length=50)
    adress = models.CharField(max_length=250)
    city = models.CharField(max_length=20)
    fono = models.CharField(max_length=10)

