from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Ambiente, Labor, Periodo, Docente, Horario
from .forms import AmbienteForm, LaborForm, PeriodoFrom, DocenteForm
from django.db.models import Q 
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import HorarioSerializer
from .facade import HorariosFacade
from django.http import JsonResponse


# Create your views here.


@login_required

def salir(request):
    logout(request)
    return redirect('/')

def nosotros(request):
    return render(request, 'plantillas/nosotros.html' )

def perfil(request):
    return render(request, 'plantillas/perfi.html')

def ambientes(request):
    busqueda = request.POST.get("buscar")
    ambientes = Ambiente.objects.all()
    if busqueda:
        ambientes = Ambiente.objects.filter(
            Q(nombre_ambiente__icontains = busqueda) |
            Q(ubicacion_ambiente__icontains = busqueda) |
            Q(capacidad_ambiente__icontains = busqueda) |
            Q(tipo_ambiente__icontains =busqueda) |
            Q(id_ambiente__icontains = busqueda)
        ).distinct()
    return render(request, 'ambientes/ambiente.html', {'ambientes': ambientes}) 

def crear_ambiente(request):
    formulario = AmbienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('ambientes')
    return render(request, 'ambientes/crear_ambiente.html', {'formulario': formulario})

def editar_ambiente(request, id_ambiente):
    ambiente = Ambiente.objects.get(id_ambiente=id_ambiente)
    formulario = AmbienteForm(request.POST or None, instance=ambiente)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('ambientes')
    return render(request, 'ambientes/editar_ambiente.html', {'formulario': formulario})

def eliminar_ambiente(request, id_ambiente):
    ambiente = Ambiente.objects.get(id_ambiente=id_ambiente)
    ambiente.delete()
    return redirect('ambientes')

#vistas de labores

def labores(request):
    busqueda = request.POST.get("buscar")
    labores = Labor.objects.all()
    if busqueda:
        labores = Labor.objects.filter(
            Q(id_labor__icontains = busqueda) |
            Q(nombre_labor__icontains = busqueda) |
            Q(tipo_labor__icontains = busqueda)
        ).distinct()
    return render(request, 'labores/labor.html', {'labores': labores})

def crear_labor(request):
    formulario2 = LaborForm(request.POST or None, request.FILES or None)
    if formulario2.is_valid():
        formulario2.save()
        return redirect('labores')
    return render(request, 'labores/crear_labor.html', {'formulario2': formulario2})

def editar_labor(request, id_labor):
    labor = Labor.objects.get(id_labor=id_labor)
    formulario2 = LaborForm(request.POST or None, instance=labor)
    if formulario2.is_valid() and request.POST:
        formulario2.save()
        return redirect('labores')
    return render(request, 'labores/editar_labor.html', {'formulario2': formulario2})

def eliminar_labores(request, id_labor):
    labor = Labor.objects.get(id_labor=id_labor)
    labor.delete()
    return redirect('labores')

#vistas de los periodos academicos 

def periodos(request):
    busqueda = request.POST.get("buscar")
    periodos = Periodo.objects.all()
    if busqueda:
        periodos = Periodo.objects.filter(
            Q(id_periodo__icontains = busqueda) |
            Q(nombre_perido__icontains = busqueda) |
            Q(fecha_inicio__icontains = busqueda) |
            Q(fecha_final__icontains = busqueda) 
        ).distinct()
    return render(request, 'periodosA/periodos.html', {'periodos': periodos})

def crear_periodo(request):
    formulario3 = PeriodoFrom(request.POST or None)
    if formulario3.is_valid():
        formulario3.save()
        return redirect('periodos')
    return render(request, 'periodosA/crear_periodo.html', {'formulario3': formulario3})

def editar_periodo(request, id_periodo):
    periodos = Periodo.objects.get(id_periodo=id_periodo)
    formulario3 = PeriodoFrom(request.POST or None, instance=periodos)
    if formulario3.is_valid() and request.POST:
        formulario3.save()
        return redirect('periodos')
    return render(request, 'periodosA/editar_periodo.html', {'formulario3': formulario3})

def eliminar_periodos(request, id_periodo):
    periodos = Periodo.objects.get(id_periodo=id_periodo)
    periodos.delete()
    return redirect('periodos')

# VISTAS DOCENTES

def docentes(request):
    busqueda = request.POST.get("buscar")
    docentes = Docente.objects.all()
    if busqueda:
        docentes = Docente.objects.filter(
            Q(id_docente__icontains = busqueda) |
            Q(nombre_docente__icontains = busqueda) |
            Q(apellido_docente__icontains = busqueda) |
            Q(identificacion_docente__icontains = busqueda) |
            Q(tipo_docente_icontains = busqueda) |
            Q(tipoContrato_docente_icontains = busqueda) |
            Q(area_docente_icontains = busqueda)
        ).distinct()
    return render(request, 'docentes/docente.html', {'docentes': docentes})

def crear_docente(request):
    formulario4 = DocenteForm(request.POST or None)
    if formulario4.is_valid():
        formulario4.save()
        return redirect('docentes')
    return render(request, 'docentes/crear_docente.html', {'formulario4': formulario4})

def editar_docentes(request, id_docente):
    docentes = Docente.objects.get(id_docente=id_docente)
    formulario4 = DocenteForm(request.POST or None, instance=docentes)
    if formulario4.is_valid() and request.POST:
        formulario4.save()
        return redirect('docentes')
    return render(request, 'docentes/editar_docente.html', {'formulario4': formulario4})

def eliminae_docente(request, id_docente):
    docentes = Docente.objects.get(id_docente=id_docente)
    docentes.delete()
    return redirect('docentes')


class HorarioViewset(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer
    
    def horario(self, request, *args, **kwargs):
        # Utilizar la fachada para obtener la lista de horarios
        horarios = HorariosFacade.obtener_horarios()
        serializer = self.get_serializer(horarios, many=True)
        return render(request, 'horarios/horario.html', {'horarios': horarios})
    
    def crear_horario(request):
        crear_horario = HorariosFacade.obtener_horarios()
        out = []
        for horari in crear_horario:
            out.append({
                'id' : horari.id_horario,
                'ambiente' : horari.ambiente,
                'labor' : horari.labor,
                'periodo' : horari.periodo,
                'docente' : horari.docente,
                'horario_dia' : horari.horario_dia.strftime("%m/%d/%Y"),
                'horario_hora_inicio' : horari.horario_hora_fin.strftime("%H:%M:%S"),
                'horario_hora_fin' : horari.horario_hora_fin.strftime("%H:%M:%S"),
                'horario_duracion' : horari.horario_duracion,   
            })
            return render(request, 'horarios/crear_horario.html')

    def add_event(request):
        id = request.GET.get("start", None)
        end = request.GET.get("end", None)
        title = request.GET.get("title", None)
        event = HorariosFacade(name=str(title), start=start, end=end)
        event.save()
        data = {}
        return JsonResponse(data)
    
    
    
    #def crear(self, request):
        # Utilizar la fachada para crear un nuevo horario
        #fachada = HorariosFacade()
        #nuevo = fachada.crear_horario(request.data)
        #return Response({"status": "Horario creado correctamente"}, status=201)
    
    