from django.db import models
from main.models import Estudiante
# Create your models here.


class Internado(models.Model):
    estudiante = models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    orden_rotativa = models.IntegerField()
    lugar = models.CharField(max_length=100)
    profesor_guia  = models.CharField(max_length=50)
    caso_clinico_conocido = models.OneToOneField('CasoCLinicoConocido', on_delete=models.CASCADE)
    caso_clinico_desconocido = models.OneToOneField('CasoCLinicoDesconocido', on_delete=models.CASCADE)
    nota = ...
    estado = ...
    

class CasoCLinicoConocido(models.Model):
    class Nivel(models.TextChoices):
        EXCELENTE = 'Excelente', 'Excelente'
        BUENO = 'Bueno', 'Bueno'
        REGULAR = 'Regular', 'Regular'
        DEFICIENTE = 'Deficiente', 'Deficiente'

    # Campos de la matriz
    presentacion_tema = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    uso_del_tiempo = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    aspectos_semiologicos = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    anamnesis = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    evaluacion_kinesica = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    diagnostico_kinesico = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    condicion_salud_contexto = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    problematica_usuario = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    relacion_evaluacion_razonamiento = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    objetivo_general = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    objetivos_especificos = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    objetivos_operacionales = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    propuesta_tratamiento_contexto = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    educacion_comunidad = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    trabajo_equipo_derivacion = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    pronostico_funcional = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    defensa_caso_clinico = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)

    def __str__(self):
        return f"Evaluación de Estudiante #{self.id}"

    
class CasoClinicoDesconocido(models.Model):
    class Nivel(models.TextChoices):
        EXCELENTE = 'Excelente', 'Excelente'
        BUENO = 'Bueno', 'Bueno'
        REGULAR = 'Regular', 'Regular'
        DEFICIENTE = 'Deficiente', 'Deficiente'

    # Campos de la matriz
    presentacion_personal_autocuidado = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    presentacion_tema_capacidad_sintesis = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    uso_del_tiempo = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    seguridad_empatia = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    anamnesis = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    evaluacion_kinesica = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    destreza_evaluacion_kinesica = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    problematica_usuario = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    diagnostico_kinesico = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    relacion_evaluacion_razonamiento = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    objetivo_general = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    objetivos_especificos = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    objetivos_operacionales = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    destreza_tecnicas_kinesicas = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    pronostico_funcional = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)
    defensa_caso_clinico = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.DEFICIENTE)

    def __str__(self):
        return f"Evaluación de Estudiante #{self.id}"

