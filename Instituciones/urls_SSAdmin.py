from django.conf.urls import url

from . import views

app_name = 'Instituciones'

urlpatterns = [

    # SSAdmin/instituciones
    url(r'^$', views.inst_SS_lists, name='inst_SS_lists'),


    # SSAdmin/inst_editar/3
    url(r'^_editar/(?P<pk>[0-9]+)/', views.inst_update.as_view(), name='inst_update')

]