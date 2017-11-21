from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'Clases'

urlpatterns =[
# ssadmin/asistencias
    url(r'^$', TemplateView.as_view(template_name='Clases/ss_asistance_list.html'), name='assistance_lists'),

# administrador/asistencias/daniel/1
    url(r'^/daniel/1/', TemplateView.as_view(template_name='Clases/ss_assistance_detail.html'),
        name='assistance_detail'),

# administrador/asistencias/1
    url(r'^1/', TemplateView.as_view(template_name='Clases/ss_assistance_confirm.html'),
        name='assistance_done'),

]