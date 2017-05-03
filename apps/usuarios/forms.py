from django import forms
from django.contrib.auth.models import User
from .models import *
 
class UserProfileForm(forms.ModelForm):
	first_name = forms.CharField(label="Nombre(s)", widget=forms.TextInput(attrs={'class':'form-control','style':'width: 400px;'}))
	last_name = forms.CharField(label="Apellido(s)", widget=forms.TextInput(attrs={'class':'form-control','style':'width: 400px;'}))
	email = forms.CharField(label="Email",widget=forms.TextInput(attrs={'class':'form-control',"placeholder":'micorreo@miservidor.com','style':'width: 400px;'}))
	class Meta:
		model  =User
		fields =['first_name','last_name','email']

class miPerdil(forms.ModelForm):
	pais = forms.CharField(label="Pais",widget=forms.TextInput(attrs={'clas':'form-control'}))

	class Meta:
		model = usuarioPerfil
		fields=['pais']