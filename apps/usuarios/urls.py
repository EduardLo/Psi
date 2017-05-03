from django.conf.urls import url
from . import views
from .views import *
from django.contrib.auth.views import login, logout_then_login

#las urls aqui
app_name='usuarios'
urlpatterns=[
	url(r'^usuarios/$',views.usuariosView,name='index'),
	url(r'^accounts/profile/(?P<pk>[\d]+)/edit/$',views.edit_user,name='user_profile_detail'),
	url(r'^accounts/profile/(?P<pk>[\d]+)/$',views.verPerfil,name='viewProfile'),
	#url(r'^(?P<pk>[0-9]+)/$',detalles,name='detail'),
]