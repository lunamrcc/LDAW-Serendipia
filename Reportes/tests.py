from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import RepoClases
from django.db.models import QuerySet

# Create your tests here.

class ReportesTest(TestCase):

    def setUp(self):
        RepoClases.objects.create(
            nombre='Gateo',
            descripcion='si sirve',
            horario='10-11',
            requisitos='No saber gatear',
        )

    def test_Clases_create(self):
        RepoClases.objects.create(
            nombre='Music',
            descripcion='Learn music',
            horario='2-3',
            requisitos='Have a guitar',
        )
        RClas_acum = RepoClases.objects.filter(nombre='Music').count()
        self.assertEqual(RClas_acum, 1)

    def test_Clases_read(self):
        RClases_all = RepoClases.objects.all()
        self.assertIsInstance(RClases_all, QuerySet)

