from django.conf.urls import url, include
from Usuarios import urls
from . import views

app_name = 'Reportes'

urlpatterns = [

    #/administrador/
    url(r'^$', views.export_users_csv, name='reportes'),

]