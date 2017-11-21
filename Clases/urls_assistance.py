from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'Assistance'

urlpatterns =[
# administrador/asistencias
    url(r'^$', views.assistance_lists, name='assistance_lists'),

# administrador/asistencias/daniel/1
    url(r'^/daniel/1/', TemplateView.as_view(template_name='Clases/admin_assistance.html'),
        name='assistance'),

# administrador/asistencias/daniel/1
    url(r'^/1/', TemplateView.as_view(template_name='Clases/admin_assistance_confirm.html'),
        name='assistance_done'),
]

