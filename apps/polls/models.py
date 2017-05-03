from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

# Create your models here.
 
@python_2_unicode_compatible
class categoria(models.Model):
	nombre_clasif=models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.nombre_clasif

@python_2_unicode_compatible
class cuestionario(models.Model):
	clasif =models.ManyToManyField(categoria,blank=True)
	nombre_test=models.CharField(max_length=150,unique=True)


	def __str__(self):
		return self.nombre_test

@python_2_unicode_compatible
class preguntas(models.Model):
	cuest = models.ForeignKey(cuestionario, on_delete=models.CASCADE)
	question_text = models.CharField(max_length=200)

	def __str__(self):
		return	self.question_text

@python_2_unicode_compatible
class choice(models.Model):
	question = models.ForeignKey(preguntas, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	value = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text

@python_2_unicode_compatible
class resultadoUsuario(models.Model): 
	usuario = models.ForeignKey(User)
	testRealizado = models.ForeignKey(cuestionario, on_delete=models.CASCADE)
	resultado = models.IntegerField(default=0)
	dateTest = models.DateTimeField('date resuelto')

	def __str__(self):
		return str(self.usuario)

@python_2_unicode_compatible
class Interpretacion(models.Model):
	prueba = models.ForeignKey(cuestionario, on_delete=models.CASCADE)
	Pmin = models.IntegerField(default=0)
	Pmax = models.IntegerField(default=0)
	diag = models.CharField(max_length=250)

	def __str__(self):
		return str(self.prueba)


"""Las cosas del invitado"""
"""Invitado"""
@python_2_unicode_compatible 
class Invitado(models.Model):
	"""docstring for """
	nombre= models.CharField(verbose_name=("Nombre Completo"),max_length=100)
	email = models.CharField(verbose_name=("Correo"),max_length=100)
	edad = models.CharField(verbose_name=("edad"),max_length=2, default=18)
	sexo = models.CharField(verbose_name=("sexo"),max_length=15, default="Hombre")
	direccion = models.CharField(verbose_name=("direccion"),max_length=255,default="local")
	telefono = models.CharField(verbose_name=("telefono"),max_length=14, default="664")
	def __str__(self):
		return self.nombre


@python_2_unicode_compatible
class resultadoGuest(models.Model):
	usuario = models.ForeignKey(Invitado,default="Invitado")
	testRealizado = models.ForeignKey(cuestionario, on_delete=models.CASCADE)
	resultado = models.IntegerField(default=0)
	dateTest = models.DateTimeField('date resuelto')

	def __str__(self):
		return str(self.usuario)

