from django.contrib import admin

from .models import *
# Register your models here.
class UsrProfileAdmin(admin.ModelAdmin):
	fields =('usuario','ciudad','pais','telefonoMovil','telefonoCasa','telefonoTrabajo','bio','inter','image','image_tag',)
	readonly_fields=('image_tag',)
	pass

admin.site.register(usuarioPerfil, UsrProfileAdmin)
