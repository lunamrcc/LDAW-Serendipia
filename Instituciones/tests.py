# Create your tests here.
from django.test import TestCase
from .models import Instituciones
from django.db.models import QuerySet

# Create your tests here.

class InstTest(TestCase):

    def setUp(self):
        Instituciones.objects.create(
            institucionID='1',
            nombre='ITESM',
            direccion='Epigmenio',
            telefono='1234',
            coordenadaX='567.0',
            coordenadaY='89.0',
        )

    def test_Instituciones_create(self):
        Instituciones.objects.create(
            institucionID='10',
            nombre='Maxei',
            direccion='Prol',
            telefono='987',
            coordenadaX='654.0',
            coordenadaY='321.0',
        )
        ssinst_acum = Instituciones.objects.filter(nombre='Maxei').count()
        self.assertEqual(ssinst_acum, 1)

    def test_Instituciones_read(self):
        ssinst_all = Instituciones.objects.all()
        self.assertIsInstance(ssinst_all, QuerySet)

    def test_Instituciones_update(self):
        ssinst = Instituciones.objects.get(nombre='ITESM')
        ssinst.direccion = 'san francisco'
        self.assertEqual(ssinst.direccion, 'san francisco')


    def test_Instituciones_delete(self):
        ssinst = Instituciones.objects.get(nombre='ITESM')
        ssinst.delete()
        ssinst_acum = Instituciones.objects.filter(nombre='ITESM').count()
        self.assertEqual(ssinst_acum, 0)
