from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Clases
from django.db.models import QuerySet

# Create your tests here.

class ClasesTest(TestCase):

    def setUp(self):
        Clases.objects.create(
            nombre='Gateo',
            descripcion='si sirve',
            horario='10-11',
            requisitos='No saber gatear',
        )

    def test_Clases_create(self):
        Clases.objects.create(
            nombre='Music',
            descripcion='Learn music',
            horario='2-3',
            requisitos='Have a guitar',
        )
        Clas_acum = Clases.objects.filter(nombre='Music').count()
        self.assertEqual(Clas_acum, 1)

    def test_Clases_read(self):
        Clases_all = Clases.objects.all()
        self.assertIsInstance(Clases_all, QuerySet)

    def test_Clases_update(self):
        Class = Clases.objects.get(nombre='Gateo')
        Class.horario = '23-24'
        self.assertEqual(Class.horario, '23-24')


    def test_Clases_delete(self):
        Class = Clases.objects.get(nombre='Gateo')
        Class.delete()
        Class_acum = Clases.objects.filter(nombre='Gateo').count()
        self.assertEqual(Class_acum, 0)
