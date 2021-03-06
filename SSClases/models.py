from django.db import models
from Estudiantes.models import Estudiantes
from Serendipia import settings

# Create your models here.

class SSClases(models.Model):


    nombre = models.CharField(
        max_length = 50,
        null = False
    )

    descripcion = models.CharField(
        max_length = 500,
        null = False
    )

    horario = models.CharField(
        max_length = 100,
        null = False
    )

    requisitos = models.CharField(
        max_length = 500,
        null = False
    )

    estudiantes = models.ManyToManyField(
        Estudiantes,
    )

    def __str__(self):
        return self.nombre
