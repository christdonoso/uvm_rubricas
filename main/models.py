from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    names = models.CharField(max_length=50)
    last_names = models.CharField(max_length=50)
    personal_info = models.TextField()
    email = models.EmailField(max_length=50)
 
