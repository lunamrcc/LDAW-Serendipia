from django.db import models

# Create your models here.

class Clases (models.Model):


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

    def __str__(self):
        return self.nombre