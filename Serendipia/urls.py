"""Serendipia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from Usuarios import views

app_name='Serendipia'

urlpatterns = [
    #admin
    url(r'^admin/', admin.site.urls),

    #login
    url(r'^login/', views.login, name='login'),

    #administrador
    url(r'^administrador/', include('Index.urls', namespace='administrador')),
    url(r'^administrador/usuarios/', include('Usuarios.urls', namespace='usuarios')),
    url(r'^administrador/estudiantes/', include('Estudiantes.urls', namespace='estudiantes')),
    url(r'^administrador/instituciones/', include('Instituciones.urls', namespace='instituciones')),
    url(r'^administrador/clases/', include('Clases.urls', namespace='clases')),
    url(r'^administrador/asistencia/', include('Clases.urls_assistance', namespace='asistance')),
    url(r'^administrador/reportes/', include('Reportes.urls', namespace='reportes')),


    #SSAdmin
    url(r'^ss/', include('Index.urls_ssadmin', namespace='ssadmin')),
    url(r'^ss/inst/', include('SSInstituciones.urls', namespace='ssinstituciones')),
    url(r'^ss/clases/', include('SSClases.urls', namespace='ssclases')),
    url(r'^ss/estudiantes/', include('SSEstudiantes.urls', namespace='ssestudiantes')),
    url(r'^ss/usuarios/', include('SSUsuarios.urls', namespace='ssusuarios')),


    #alumnos
    url(r'^alumnos/', include('Index.urls_alumnos', namespace='alumnos')),
    url(r'^alumnos/clases', include('Clases.urls_alumnos', namespace='alumnos_clases')),

]
