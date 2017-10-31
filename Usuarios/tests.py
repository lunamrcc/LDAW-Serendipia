from django.test import TestCase
from .models import Usuarios
from django.db.models import QuerySet

# Create your tests here.

class UsuariosTest(TestCase):

    def setUp(self):
        Usuarios.objects.create(
            Nombre='Jimena',
            Apaterno='Luna',
            Amaterno='Calvillo',
            Telefono='4422580662',
            Email='jluna@icloud.com',
            Passwd='l',
            Activo=True,
        )

    def test_Usuarios_create(self):
        Usuarios.objects.create(
            Nombre='Mariano',
            Apaterno='Luna',
            Amaterno='Calvillo',
            Telefono='4422580662',
            Email='mariano@icloud.com',
            Passwd='l',
            Activo=True,
        )
        User_acum = Usuarios.objects.filter(Email='mariano@icloud.com').count()
        self.assertEqual(User_acum, 1)

    def test_Usuarios_read(self):
        Usuarios_all = Usuarios.objects.all()
        self.assertIsInstance(Usuarios_all, QuerySet)

    def test_Usuarios_update(self):
        Usu = Usuarios.objects.get(Email='jluna@icloud.com')
        Usu.Nombre = 'Ximena'
        self.assertEqual(Usu.Nombre, 'Ximena')

    def test_Usuarios_unactive(self):
        Usu = Usuarios.objects.get(Email='jluna@icloud.com')
        Usu.Activo = False
        self.assertEqual(Usu.Activo, False)

    def test_Usuarios_active(self):
        Usu = Usuarios.objects.get(Email='jluna@icloud.com')
        Usu.Activo = True
        self.assertEqual(Usu.Activo, True)

    def test_Usuarios_delete(self):
        Usu = Usuarios.objects.get(Email='jluna@icloud.com')
        Usu.delete()
        User_acum = Usuarios.objects.filter(Email='jluna@icloud.com').count()
        self.assertEqual(User_acum, 0)
