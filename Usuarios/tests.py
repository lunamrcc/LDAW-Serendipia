from django.test import TestCase
from .models import Usuarios
from Clases.models import Asistencia, Clases
from Instituciones.models import Instituciones
from Estudiantes.models import Estudiantes
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

        Instituciones.objects.create(
            institucionID=1,
            nombre='ESKALA',
            direccion='Acordada 25',
            telefono='442258',
            coordenadaX=500,
            coordenadaY=200
        )

        Clases.objects.create(
            nombre='Arte',
            descripcion='Oleo',
            horario='Jueves 8:00 - 10:00',
            requisitos='Pintura experiencia',
        )

        Estudiantes.objects.create(
            EstudianteID=1,
            Nombre='Armando',
            aPaterno='Hoyos',
            aMaterno='Yaaa',
            Telefono='4422580662',
            Escuela='ITESM',
            Correo='luna@luna.com',
            Passwd='luna',
            Activo=True
        )

    def test_login(self):
        User_acum = Usuarios.objects.filter(Email='jluna@icloud.com').count()
        self.assertEqual(User_acum, 1)

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

    def test_logout(self):
        User_acum = Usuarios.objects.filter(Email='jlunac@icloud.com').count()
        self.assertEqual(User_acum, 0)

    def test_Usuarios_active(self):
        Usu = Usuarios.objects.get(Email='jluna@icloud.com')
        Usu.Activo = True
        self.assertEqual(Usu.Activo, True)

    def test_Usuarios_delete(self):
        Usu = Usuarios.objects.get(Email='jluna@icloud.com')
        Usu.delete()
        User_acum = Usuarios.objects.filter(Email='jluna@icloud.com').count()
        self.assertEqual(User_acum, 0)

    def test_register_assistance(self):
         Asistencia.objects.create(
             Estudiante=Estudiantes.objects.get(Nombre='Armando'),
             Clase=Clases.objects.get(nombre='Arte'),
             Latitud=500,
             Longitud=100,
         )

    def test_SSAdmin_Users(self):
        Usuarios_all = Usuarios.objects.all()
        self.assertIsInstance(Usuarios_all, QuerySet)


    def test_Student_unactive(self):
        Usu = Estudiantes.objects.get(Correo='luna@luna.com')
        Usu.Activo = False
        self.assertEqual(Usu.Activo, False)

    def test_Student_active(self):
        Usu = Estudiantes.objects.get(Correo='luna@luna.com')
        Usu.Activo = True
        self.assertEqual(Usu.Activo, True)

    def test_Student_classes(self):
        User_acum = Clases.objects.all().count()
        self.assertEqual(User_acum, 1)

    def test_Assistance_SSAdmin(self):
        aux = Asistencia.objects.filter(Estudiante=Estudiantes.objects.get(Nombre='Armando'))
        aux.SSAdmin = True
        self.assertEqual(aux.SSAdmin, 1)

    def test_Assistance_all(self):
        Asistencia_all = Asistencia.objects.all()
        self.assertIsInstance(Asistencia_all, QuerySet)

    def test_Assistance_Admin(self):
        aux = Asistencia.objects.filter(Estudiante=Estudiantes.objects.get(Nombre='Armando'))
        aux.Admin = True
        self.assertEqual(aux.Admin, True)