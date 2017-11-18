from django.conf.urls import url, include
from Usuarios import urls
from . import views

app_name = 'Index'

urlpatterns = [

    #/SSAdmin/
    url(r'^$', views.Index_SSAdmin, name='dashboard_SSAdmin'),
]
