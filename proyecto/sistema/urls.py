from django.urls import path, include
from rest_framework import routers
from . import views
from .views import HorarioViewset

router = routers.DefaultRouter()
router.register(r'horario', views.HorarioViewset)


urlpatterns = [
    
    path('', views.nosotros, name="inicio"),
    path('', include(router.urls)),
    path('perfil', views.perfil, name="perfil"),
    path('salir/', views.salir, name="salir"),

    #url de ambientes 

    path('ambientes', views.ambientes, name="ambientes"),
    path('crear', views.crear_ambiente, name="crear_ambiente"),
    path('editar_ambiente', views.editar_ambiente, name="editar_ambiente"),
    path('eliminar_ambiente/<int:id_ambiente>', views.eliminar_ambiente, name="eliminar_ambiente"),
    path('editar_ambiente/<int:id_ambiente>', views.editar_ambiente, name="editar_ambiente"),

    #urls de labores

    path('labores', views.labores, name="labores"),
    path('crear_labor', views.crear_labor, name="crear_labor"),
    path('editar_labor', views.editar_labor, name="editar_labor"),
    path('eliminar_labor/<int:id_labor>', views.eliminar_labores, name="eliminar_labor"),
    path('editar_labores/<int:id_labor>', views.editar_labor, name="editar_labor"),

    #urls de los periodos academicos 

    path('periodos', views.periodos, name="periodos"),
    path('crear_periodo', views.crear_periodo, name="crear_periodo"),
    path('editar_periodo', views.editar_periodo, name="editar_periodo"),
    path('eliminar_periodo/<int:id_periodo>', views.eliminar_periodos, name="eliminar_periodo"),
    path('editar_periodo/<int:id_periodo>', views.editar_periodo, name="editar_periodo"),
    
    path('docentes', views.docentes, name="docentes"),
    path('crear_docente', views.crear_docente, name="crear_docente"),
    path('editar_docente', views.editar_docentes, name="editar_docente"),
    path('eliminar_docente/<int:id_docente>', views.eliminae_docente, name="eliminar_docente"),
    path('editar_docente/<int:id_docente>', views.editar_docentes, name="editar_docente"),

    path('horarios/', HorarioViewset.as_view({'get': 'horario'}), name='ver_horarios'),
]

