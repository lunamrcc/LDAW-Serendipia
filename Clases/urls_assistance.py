from django.conf.urls import url

from . import views

app_name = 'Assistance'

urlpatterns =[
# administrador/asistencias
    url(r'^$', views.assistance_lists, name='assistance_lists')
]