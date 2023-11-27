from django import forms
from .models import Ambiente,Labor, Periodo, Docente
from django.core.exceptions import ValidationError
from datetime import timedelta


class AmbienteForm(forms.ModelForm):
    class Meta:
        model = Ambiente
        fields = '__all__'

class LaborForm(forms.ModelForm):
    class Meta:
        model = Labor
        fields = '__all__'

class PeriodoFrom(forms.ModelForm):
    class Meta:
        model = Periodo
        fields = ['nombre_perido', 'fecha_inicio']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
        }

    def save(self):
        fecha_inicio = self.cleaned_data.get('fecha_inicio')
        fecha_final = fecha_inicio + timedelta(days=135)

        periodo = Periodo(
         nombre_perido = self.cleaned_data['nombre_perido'], 
         fecha_inicio=fecha_inicio,
         fecha_final=fecha_final 
      )

        periodo.save()
            
        return periodo
    
class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'