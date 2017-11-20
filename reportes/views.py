from django.shortcuts import render

# Create your views here.

import csv

from django.http import HttpResponse
from Clases.models import Clases, Asistencia

def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="asistencias.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nombre Estudiante', 'Clase', 'Fecha', 'Admin', 'SS Admin', 'Horas'])

    users = Asistencia.objects.all().values_list('Estudiante', 'Clase', 'Fecha', 'Admin', 'SS_Admin', 'Horas')
    for user in users:
        writer.writerow(user)

    return response