from django.contrib import admin
from .models import * #Se puede poner .models ya que estámos llamando a models pero este está en la misma carpeta.

# Register your models here.

admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Entregable)
admin.site.register(Profesor)
admin.site.register(Certificaciones)