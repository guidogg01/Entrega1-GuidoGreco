from django.urls import path
from AppCoder import views


urlpatterns = [

    path("cursos/", views.curso, name = "Cursos"),
    path("estudiante/", views.estudiante, name = "Estudiantes"),
    path("entregable/", views.entregable, name = "Entregables"),
    path("profesor/", views.profesor, name = "Profesores"),
    path("", views.inicio, name = "Inicio"),
    path("cursoFormulario/", views.cursoFormulario, name="CursoFormulario"),
    path("busquedaCamada/", views.busquedaCamada, name="BusquedaCamada"),
    path("buscar/", views.buscar),
]
