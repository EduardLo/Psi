from django.contrib import admin

from .models import *
# Register your models here.
class ChoiceInLine(admin.TabularInline):
	model = choice
	extra =4

class questionAdmin(admin.ModelAdmin):
	fieldsets=[
		(None, {'fields':['question_text']}),
		('cuestionario',{'fields':['cuest']})
	]
	inlines=[ChoiceInLine]
	list_display=('question_text',)
	search_fields=['question_text']


admin.site.register(categoria)
admin.site.register(cuestionario)
admin.site.register(preguntas,questionAdmin)
admin.site.register(choice)
admin.site.register(resultadoUsuario)
admin.site.register(Interpretacion)
admin.site.register(resultadoGuest)
admin.site.register(Invitado)