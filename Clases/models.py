from django.db import models
from Estudiantes.models import Estudiantes
from Serendipia import settings

# Create your models here.

class Clases(models.Model):


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


class Asistencia(models.Model):

    Estudiante = models.ForeignKey(Estudiantes,
                                   on_delete=models.CASCADE)

    Clase = models.ForeignKey(Clases,
                              on_delete=models.CASCADE)

    Fecha = models.DateTimeField(auto_now=True)

    Latitud = models.DecimalField(
        null = False,
        max_digits = 10,
        decimal_places = 5
    )

    Longitud = models.DecimalField(
        null = False,
        max_digits = 10,
        decimal_places = 5
    )

    Admin = models.BooleanField(
        default=False
    )

    SS_Admin = models.BooleanField(
        default=False
    )

    Horas = models.IntegerField(
        null = True,
        blank = True
    )

    def __str__(self):
        return self.Fecha
