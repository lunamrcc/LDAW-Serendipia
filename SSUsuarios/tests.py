from django.test import TestCase
from .models import SSUsuarios
from django.db.models import QuerySet

# Create your tests here.

class SSUsuariosTest(TestCase):

    def setUp(self):
        SSUsuarios.objects.create(
            Nombre='Jimena',
            Apaterno='Luna',
            Amaterno='Calvillo',
            Telefono='4422580662',
            Email='jluna@icloud.com',
            Passwd='l',
            Activo=True,
        )


    def test_SSUsuarios_read(self):
        Usuarios_all = SSUsuarios.objects.all()
        self.assertIsInstance(Usuarios_all, QuerySet)