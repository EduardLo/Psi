from django import forms
from .models import *


class InvitadoRegistro(forms.Form):
	nombre= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',"placeholder":'Nombre Completo','id':'idNaombreGuest'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control',"placeholder":'Correo Electroico','id':'idNaombreGuest'}))