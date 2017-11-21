# Create your tests here.
from django.test import TestCase
from .models import SSClases
from django.db.models import QuerySet

# Create your tests here.

class SSClasesTest(TestCase):

    # def setUp(self):
    #     SSClases.objects.create(
    #         nombre='Gateo',
    #         descripcion='si sirve',
    #         horario='10-11',
    #         requisitos='No saber gatear',
    #     )
    #
    # def test_SSClases_create(self):
    #     SSClases.objects.create(
    #         nombre='Music',
    #         descripcion='Learn music',
    #         horario='2-3',
    #         requisitos='Have a guitar',
    #     )
    #     Clas_acum = SSClases.objects.filter(nombre='Music').count()
    #     self.assertEqual(Clas_acum, 1)

    def test_SSClases_read(self):
        Clases_all = SSClases.objects.all()
        self.assertIsInstance(Clases_all, QuerySet)

    # def test_Clases_update(self):
    #     Class = SSClases.objects.get(nombre='Gateo')
    #     Class.horario = '23-24'
    #     self.assertEqual(Class.horario, '23-24')


    # def test_SSClases_delete(self):
    #     Class = SSClases.objects.get(nombre='Gateo')
    #     Class.delete()
    #     Class_acum = SSClases.objects.filter(nombre='Gateo').count()
    #     self.assertEqual(Class_acum, 0)
