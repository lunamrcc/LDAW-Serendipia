from django.conf.urls import url, include
from Usuarios import urls
from . import views

app_name = 'Index'

urlpatterns = [

    #/alumno/
    url(r'^$', views.Index_ssadmin, name='dashboard_ssadmin'),
]