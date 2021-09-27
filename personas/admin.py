from django.contrib import admin

# Register your models here
from personas.models import Domicilio, Persona, Ocupacion, Registro

admin.site.register(Domicilio)
admin.site.register(Persona)
admin.site.register(Ocupacion)
admin.site.register(Registro)
