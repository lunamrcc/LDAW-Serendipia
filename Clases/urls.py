from django.conf.urls import url

from . import views

app_name = 'Clases'

urlpatterns = [
    #administrador/clases
    url(r'^$', views.class_lists, name='class_lists'),

    #administrador/clases/3/delete
    url(r'^(?P<pk>[0-9]+)/eliminar/$', views.class_delete, name='class_delete'),

    # administrador/clases/crear
    url(r'^crear/$', views.class_create, name='class_create'),

    # administrador/clases_editar/3
    url(r'^editar/(?P<pk>[0-9]+)/', views.class_update.as_view(), name='class_update'),

]




