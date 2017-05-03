from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.views.generic import *
from django import forms

# Create your views here.

def usuariosView(request):
	usr = User.objects.all()
	template_name = 'usuarios/usrList.html'
	return render(request,template_name,{'usr_list':usr,})


class profileView(DetailView):
	"""docstring for profileView"""
	model = usuarioPerfil
	template_name='usuarios/usuario_perfil.html'
	

@login_required()
def edit_user(request,pk):
	user = User.objects.get(pk=pk)

	user_form=UserProfileForm(instance=user)

	ProfileInlineFormset=inlineformset_factory(User,usuarioPerfil,
		fields=('ciudad',
		'pais','telefonoMovil','telefonoCasa','telefonoTrabajo','image','inter'),
		labels={
		'ciudad': 'Ciudad',
		'pais': 'Pais',
		'telefonoMovil': 'Telefono Movil',
		'telefonoCasa': 'Telefono de Casa',
		'telefonoTrabajo': 'Telefono de Trabajo',
		'image': 'Foto de Perfil',
		'inter': 'Intereses',
		},
		widgets={
		'ciudad': forms.TextInput(attrs={'class':'form-control', 'style':'width: 400px;',}),
		'pais':  forms.TextInput(attrs={'class':'form-control','style':'width: 400px;'}),
		'telefonoMovil': forms.TextInput(attrs={'class':'form-control','style':'width: 400px;'}),
		'telefonoCasa': forms.TextInput(attrs={'class':'form-control','style':'width: 400px;'}),
		'telefonoTrabajo': forms.TextInput(attrs={'class':'form-control','style':'width: 400px;'}),
		'inter': forms.Textarea(attrs={'class':'form-control','style':'width: 400px;'}),
		#'telefonoMovil': forms.CharField(label = "Telefono Movil", widget=forms.TextInput(attrs={'class':'form-control', 'style':'width: 300px;'})),
		}, can_delete=False)
	formset=ProfileInlineFormset(instance=user)

	if request.user.is_authenticated() and request.user.id == user.id:
		if request.method == "POST":
			user_form =UserProfileForm(request.POST, request.FILES, instance=user)
			formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

			if user_form.is_valid():
				created_user = user_form.save(commit=False)
				formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

				if formset.is_valid():
					created_user.save()
					formset.save()
					return HttpResponseRedirect('/accounts/profile/')
		return render(request, 'usuarios/usuario_perfil.html',{"noodle":pk, "noodle_form":user_form, "formset":formset})
	else:
		raise PermissionDenied


@login_required()
def verPerfil(request,pk):
	user = User.objects.get(pk=pk)
	user_profile = usuarioPerfil.objects.get(usuario=user.id)
	template_name = "usuarios/perfilview.html"

	return	render(request,template_name,{'usuario':user,'perfil':user_profile,})