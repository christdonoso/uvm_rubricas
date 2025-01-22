from django.db import models
from main.models import Estudiante
# Create your models here.


class Internado(models.Model):
    estudiante = models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    orden_rotativa = models.IntegerField()
    lugar = models.CharField(max_length=100)
    profesor_guia  = models.CharField(max_length=50)
    
