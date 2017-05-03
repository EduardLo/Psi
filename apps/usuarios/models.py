from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.db.models.signals import post_save
from django.utils.safestring import mark_safe

# Create your models here.  

def path(self, filename):
	path_file = "Multimedia/Users/%s/%s" % (self.usuario.username, filename)
	return path_file

@python_2_unicode_compatible 
class usuarioPerfil(models.Model):
	usuario = models.OneToOneField(User, related_name='profile')
	telefonoMovil = models.CharField(max_length=13)
	telefonoCasa = models.CharField(max_length=10)
	telefonoTrabajo = models.CharField(max_length=13)
	image = models.ImageField(verbose_name=("Foto de Perfil"),upload_to=path, default='Multimaedia/Users/unknow/user.jpg')
	ciudad = models.CharField(max_length=50, default=" ")
	pais = models.CharField(max_length=50, default=" ")
	bio = models.CharField(max_length=255, default="sobre mi")
	inter = models.CharField(max_length=255, default="mis gustos")

	def __str__(self):
		return	self.usuario.username
	
	def image_tag(self):
		return mark_safe('<img src="media/%s" width="150" height="150" />' % (self.image))
	image_tag.short_description = 'Image'

def create_profile(sender, **kwargs):
	user=kwargs["instance"]
	if kwargs["created"]:
		user_profile = usuarioPerfil(usuario=user)
		user_profile.save()

post_save.connect(create_profile,sender=User)



