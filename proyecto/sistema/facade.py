from .models import Labor, Docente, Ambiente, Periodo, Horario

class HorariosFacade:
    @staticmethod
    def obtener_ambientes():
        return Ambiente.objects.all()
    
    @staticmethod
    def obtener_labores():
        return Labor.objects.all()
    
    @staticmethod
    def obtener_periodos():
        return Periodo.objects.all()
    
    @staticmethod
    def obtener_docentes():
        return Docente.objects.all()
    
    @staticmethod
    def obtener_horarios():
        return Horario.objects.all()
    
    @staticmethod
    def crear_horario(ambiente, labor, periodo, docente, dia, hora_inicio, hora_fin, duracion):
        horario = Horario(
            ambiente=ambiente,
            labor=labor,
            periodo=periodo,
            docente=docente,
            horario_dia=dia,
            horario_hora_inicio=hora_inicio,
            horario_hora_fin=hora_fin,
            horario_duracion=duracion
        )
        horario.save()
        return horario