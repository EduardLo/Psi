from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.views.generic import *
from django.utils import timezone

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

#cosas de usuarios
from django.contrib.auth.models import User
from django.contrib import auth
from django.db.models import Count
#decorador
from django.contrib.auth.decorators import login_required

#from django.contrib.auth.views import login, logout_then_login
#los modelos
from .models import *
from .forms import *

from django.core.mail import EmailMessage
# Create your views here. 

#login y logout
"""
class DetailView(generic.ListView):
	template_name='polls/index.html'
	context_object_name ='question_list'

	def get_queryset(self):
		return preguntas.objects.all
"""
def detalles(request):
	cuest=1
	model = preguntas
	template_name = 'polls/index.html'
	question = preguntas.objects.filter(cuest=cuest)
	return render(request,template_name,{'question_list':question,'test_id':cuest,})

#@login_required
class IndexView(ListView):
	template_name='polls/cuestionarios.html'
	context_object_name='cuestionarios_list'

	def get_queryset(self):
		return cuestionario.objects.all()

@login_required
def resultado(request,test_id):
	question = preguntas.objects.filter(cuest=test_id)
	prueba = get_object_or_404(cuestionario,pk=test_id)
	try:
		total = request.POST['total']
		usr = request.POST['usuario']
		testU = test_id
		date = timezone.now()

		#guardar el modelo
		r = resultadoUsuario()
		r.usuario = User.objects.get(username=usr)
		r.testRealizado = prueba
		r.resultado = total
		r.dateTest = date
		r.save() 

		resumen = resultadoUsuario.objects.get(usuario=r.usuario, testRealizado=r.testRealizado,dateTest=r.dateTest)
	except (KeyError):
		template_name = 'polls/index.html'
		return render(request,template_name,{'question_list':question, 'error_message': prueba.nombre_test,})
	else:
		resumen = resultadoUsuario.objects.get(usuario=r.usuario,testRealizado=r.testRealizado,dateTest=r.dateTest)
		return HttpResponseRedirect(reverse('polls:resultado',args=(resumen.id,)),{'rest':resumen.id})


def ResultsView(request,pk):
	template_name="polls/results.html"
	resumen = resultadoUsuario.objects.get(pk=pk)
	iterpretaciones = Interpretacion.objects.filter(prueba=resumen.testRealizado)
	usuario_id =  User.objects.get(username=resumen.usuario)
	usuario_id=int(usuario_id.id)
	for x in iterpretaciones:
		if resumen.resultado >= x.Pmin:
			if resumen.resultado<=x.Pmax:
				tToal = x.diag
	
	email_body_template= 'polls/resultado_mail.txt'
	email_subject_template = 'polls/resultado_mail_subject.txt'
	site = get_current_site(request)
	#renderizar el correo


	asunto = render_to_string(email_subject_template) #"Resultado de Prueba ' %s" %s r.testRealizado 
	asunto = ''.join(asunto.splitlines())

	mensaje = render_to_string(email_body_template,{'usuario':resumen.usuario,'prueba':resumen.testRealizado,
			'resultado': tToal, 'site':site})
	#Enviar Email
	correo = User.objects.get(username=resumen.usuario)
	correo = correo.email
	mail = EmailMessage(asunto,mensaje, to=[correo])
	mail.send()
	
	return render(request,template_name,{'resumen':tToal,'id':resumen,'idusuario':usuario_id,})


def multipleResultado(request,user_id):
	template_name = "polls/MultipleResultado.html"
	rest_list = resultadoUsuario.objects.filter(usuario=user_id)
	user_id = int(user_id)
	return render(request,template_name,{'lista':rest_list,'idbuscado':user_id,})

"""Invitado"""
"""
def resultadoGuest(request,test_id):
	question = preguntas.objects.filter(cuest=test_id)
	prueba = get_object_or_404(cuestionario,pk=test_id)
	try:
		#total=request.POST['total_test']
		testU = test_id
		date = timezone.now()
	except (KeyError):
		template_name="polls/index.html"
		return render(request,template_name,{'question_list':question,'error_message': prueba.nombre_test,})
	else:
		return HttpResponseRedirect(reverse('polls:registroGuest',args=(test_id)),{'test_id':testU,'data':date})

def registroGuest(request,test_id):
	template_name="polls/registroGuest.html"
	testU = test_id
	formulario = InvitadoRegistro()
	if request.method =="POST":
		formulario=InvitadoRegistro(request.POST)
		if formulario.is_valid():
			try:
				nombre = formulario.cleaned_data['nombre']
				email = formulario.cleaned_data['email']
				#total = formulario.cleaned_data['totalFinal']
				date = formulario.cleaned_data['dateFinal']
				
				#furmulario de registro de invitado
				guest = Invitado()
				guest.nombre = nombre
				guest.email = email
				guest.save()

				#formulario de evaluacion
				r = resultadoGuest()
				r.usuario = Invitado.objects.get(nombre=guest.nombre,email=guest.email)
				r.testRealizado = test_id
				r.resultado = total
				r.dateTest = timezone.now()
				r.save()
			except(KeyError):
				template_name = "polls/index.hml"
				return render(request,template_name,{'question_list':question,'error_message': pueba.nombre_test,})
			else:
				resumen = resultadoGuest.objects.get(usuario=r.usuario,testRealizado=r.testRealizado,dateTest=r.dateTest)
				return HttpResponseRedirect(reverse('polls:finalGuest',args=(resumen.id,)),{'rest':resumen.id})

	else:
		formulario=Invitado()
	formulario =InvitadoRegistro()
	return	render(request,template_name,{'form':formulario,'test_id':testU})

def ResultsGuestView(request,pk):
	template_name="polls/resultsGuest.html"
	resumen = resultadoGuest.objects.get(pk=pk)
	iterpretaciones = Interpretacion.objects.filter(prueba=resumen.testRealizado)
	usuario_id =  Invitado.objects.get(nombre=resumen.usuario)
	usuario_id=int(usuario_id.id)
	for x in iterpretaciones:
		if resumen.resultado >= x.Pmin:
			if resumen.resultado<=x.Pmax:
				tToal = x.diag
	return render(request,template_name,{'resumen':tToal,'id':resumen,'usuario':usuario_id,})
"""
def listaGuest(request):
	template_name ="polls/listaguest.html"
	guests = Invitado.objects.all() .values('nombre','email').annotate(total=Count('nombre')).order_by('-nombre')
	return render(request,template_name,{'guest_lista':guests})


def finalGuest(request,test_id):
	if request.method == "POST":
		#captura los datos del invitado
		correo = request.POST['correo']
		usuario = request.POST['usuario']
		sexo = request.POST['sexo']
		direccion = request.POST['direccion']
		edad = request.POST['edad']
		telefono = request.POST['telefono']
		#guardar invitado
		i = Invitado()
		i.nombre= usuario
		i.email = correo
		i.sexo = sexo
		i.direccion = direccion
		i.edad = edad
		i.telefono = telefono
		i.save()

		#capturar datos del test (total y test realizado)
		question = preguntas.objects.filter(cuest=test_id)
		total = request.POST['total']
		date = timezone.now()

		#guardar modelo
		r = resultadoGuest()
		r.usuario = Invitado.objects.filter(nombre=usuario, email=correo)[:1].get()
		r.testRealizado = get_object_or_404(cuestionario,pk=test_id)
		r.resultado = total
		r.dateTest = date
		r.save()

		resumen = resultadoGuest.objects.get(usuario=r.usuario,testRealizado=r.testRealizado,dateTest=r.dateTest)

		#buscar interpretacion
		interpretaciones = Interpretacion.objects.filter(prueba=resumen.testRealizado)
		for x in interpretaciones:
			if resumen.resultado >=x.Pmin:
				if resumen.resultado <=x.Pmax:
					inter = x.diag

		email_body_template= 'polls/resultado_mail.txt'
		email_subject_template = 'polls/resultado_mail_subject.txt'
		site = get_current_site(request)
		#renderizar el correo


		asunto = render_to_string(email_subject_template) #"Resultado de Prueba ' %s" %s r.testRealizado 
		asunto = ''.join(asunto.splitlines())

		mensaje = render_to_string(email_body_template,{
			'usuario':usuario, 'correo': correo ,'telefono':telefono, 'direccion':direccion,'fecha':date,
			'prueba':r.testRealizado,
			'resultado': inter, 'site':site})
		#Enviar Email
		mail = EmailMessage(asunto,mensaje, to=[correo])
		mail.send()
	else:
		return HttpResponseRedirect('/')
	return render(request,'polls/exito.html',{'usuario':usuario, 'correo': correo,})


def resultadoIndividual(request,usuario,correo):
	template_name = "polls/restUser.html"
	usuario = Invitado.objects.filter(nombre=usuario, email=correo)[:1].get()
	resumen = resultadoGuest.objects.filter(usuario=usuario)
	inter = Interpretacion.objects.all()

	return render(request,template_name,{'resumen':resumen, 'inter':inter, 'usuario': usuario,})