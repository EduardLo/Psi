from django.conf.urls import url
from . import views 
from .views import *
from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.decorators import login_required

#aqui las urls
app_name='polls'
urlpatterns=[
	url(r'^$',views.detalles,name='index'),
	#url(r'^(?P<pk>[0-9]+)/$',detalles,name='detail'),
	#url(r'^(?P<pk>[0-9]+)/resultado/$',views.ResultsView.as_view(),name='resultado'),
	url(r'^(?P<pk>[0-9]+)/resultado/$',login_required(views.ResultsView),name='resultado'),
	url(r'^(?P<test_id>[0-9]+)/rest/$',views.resultado,name='rest'),

	url(r'^(?P<user_id>[0-9]+)/listRest/$',views.multipleResultado,name='resultados'),

	#invitado
	#url(r'^(?P<test_id>[0-9]+)/restInvitado/$',views.resultadoGuest,name='restInvitado'),
	#url(r'^(?P<test_id>[0-9]+)/regInvitado/$',views.registroGuest,name='registroGuest'),
	#url(r'^(?P<pk>[0-9]+)/restFinal/$',views.ResultsGuestView,name='finalGuest'),
	#login y logout
	#url(r'^accounts/login/',login,{'template_name':'polls/login.html'},name='login'),
    #url(r'^logout/$',logout_then_login,name='logout'),
    #Invitado
    url(r'^(?P<test_id>[0-9]+)/Guest/$',views.finalGuest,name='ultimoGuest'),
    url(r'^guests/$',views.listaGuest,name='listaguests'),
    url(r'^(?P<usuario>[^/]+)/rest/(?P<correo>[^/]+)/$',views.resultadoIndividual,name='restespecifico'),
] 