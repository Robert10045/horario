from django.contrib import admin
from .models import Usuario, Ambiente, Labor, Periodo, Docente, Horario

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Ambiente)
admin.site.register(Labor)
admin.site.register(Periodo)
admin.site.register(Docente)
admin.site.register(Horario)
