from django.conf.urls import url

from . import views

app_name = 'Clases'

urlpatterns = [
    # estudiante/clases/1/
    url(r'^/(?P<pk>[0-9]+)/', views.student_class_lists, name='student_class'),

    #estudiante/clases/1/asistencia_registrada
    url(r'^/(?P<pk>[0-9]+)/asistencia_registrada/', views.student_assistance, name='student_assistance'),

    # estudiante/clases/1/
    # url(r'^/(?P<EstudianteID>[0-9]+)/(?P<pk>[0-9]+)/(?P<lat>[0-9]+)/(?P<lon>[0-9]+)/',
    #     views.student_class_lists, name='student_assistance'),
]