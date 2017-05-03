from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.views.generic import *
from django.utils import timezone
from django.template import RequestContext

#cosas de usuarios
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import *
#decorador
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import logout
from registration.forms  import *
#los modelos
#from .models import *

def login_user(request):
	message = None
	form = Login_form(request.POST or None)
	form_register = MyRegistrationForm(request.POST or None)
	if request.POST and form.is_valid():
		#user=form.login(request)
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		next_page = request.POST.get('next','')

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				if next_page == "":
					next_page="/"
				return HttpResponseRedirect(next_page)
		else:
			message = 'Usuario o Password incorrectos'
	#form = Login_form()
	return render(request,'registration/login.html',{'form':form, 'registro': form_register, 'alert': message, 'next': request.GET.get('next','')})

#def logout(request):
#    auth.logout(request)
    # Redirect to a success page.
 #   return HttpResponseRedirect("/account/loggedout/")