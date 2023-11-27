from typing import Any
from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    usuario_login = models.CharField(max_length=100)
    usuario_password = models.CharField(max_length=100)

class Ambiente(models.Model):
    id_ambiente = models.CharField(max_length=6, primary_key=True)
    nombre_ambiente = models.CharField(max_length=100)
    ubicacion_ambiente = models.CharField(max_length=100)
    tipo_ambiente = models.CharField(max_length=30)
    capacidad_ambiente = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre_ambiente
    
class Labor(models.Model):
    id_labor = models.AutoField(primary_key=True)
    nombre_labor = models.CharField(max_length=100)
    tipo_labor = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_labor
    
class Periodo(models.Model):
    id_periodo = models.AutoField(primary_key=True)
    nombre_perido = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()

    def __str__(self):
        return self.nombre_perido

class Docente(models.Model):
    id_docente = models.AutoField(primary_key=True)
    nombre_docente = models.CharField(max_length=100)
    apellido_docente = models.CharField(max_length=100)
    tipo_identificacion = models.CharField(max_length=10)
    identificacion_docente = models.IntegerField()
    tipo_docente = models.CharField(max_length=100)
    tipoContrato_docente = models.CharField(max_length=100)
    area_docente = models.CharField(max_length=100)

    def __str__(self): 
        return self.nombre_docente
    
class Horario(models.Model):
    id_horario = models.AutoField(primary_key=True)
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    labor = models.ForeignKey(Labor, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    horario_dia = models.DateField()
    horario_hora_inicio = models.TimeField()
    horario_hora_fin = models.TimeField()
    horario_duracion = models.DurationField()

    def __str__(self):
         return str(self.id_horario)