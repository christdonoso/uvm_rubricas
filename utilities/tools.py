"""
Funciones de utilidad para diferentes tareas
"""
from django.db import models

#lambda para formatear un string con el rut ej 123456789 --> 12.345.678-9
format_rut = lambda x: f'{int(x[:-1]):,}-{x[-1]}'.replace(',','.')

#lambda para eliminar el csrf_token de una request de django
remove_csrftoken = lambda x:{k:v for k,v in x.items() if k != 'csrfmiddlewaretoken'}


def update_model_object(obj:models, data:dict):
    """
    funcion que toma un model object y un diccionario, modifica
    los atributos del modelo con los datos del diccionario y guarda el modelo
    
        obj (models): django models object
        data (dict): dict
    """
    for k,v in data.items():
        setattr(obj, k,v)
    obj.save()
