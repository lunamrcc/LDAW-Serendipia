from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'Clases'

urlpatterns = [
    # estudiante/clases/1/
    url(r'^/(?P<pk>[0-9]+)/', views.student_class_lists, name='student_class'),

    #estudiante/clases/1/asistencia_registrada
    url(r'^/asistencia/', TemplateView.as_view(template_name='Clases/student_assistance.html')
        , name='student_assistance'),

    # estudiante/clases/1/
    # url(r'^/(?P<EstudianteID>[0-9]+)/(?P<pk>[0-9]+)/(?P<lat>[0-9]+)/(?P<lon>[0-9]+)/',
    #     views.student_class_lists, name='student_assistance'),
]