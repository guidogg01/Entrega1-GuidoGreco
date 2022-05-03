from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.forms import CursoFormulario
from AppCoder.models import Curso

def curso(request):

    if request.method == "POST": #Al hacer click en enviar.

        miFormulario = CursoFormulario(request.POST) #Aquí llega la info del formulario

        print (miFormulario)

        if miFormulario.is_valid(): #Comprobamos si la info es valida

            informacion = miFormulario.cleaned_data

            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"], duracion=informacion["duracion"]) #Creamos un curso (modelo) usando la info recibida.

            curso.save()

            return render(request, "AppCoder/inicio.html") #Una vez guardado, mostramos la plantilla de inicio.
    
    else:

        miFormulario = CursoFormulario() #Me muestra un formlario vacío.
    
    return render(request,"AppCoder/curso.html", {"miFormulario":miFormulario})

def estudiante(request):

    return render(request,"AppCoder/estudiante.html")

def entregable(request):

    return render(request,"AppCoder/entregable.html")

def profesor(request):

    return render(request,"AppCoder/profesor.html")

def inicio(request):

    return render(request,"AppCoder/inicio.html")

def cursoFormulario(request):
    return

def busquedaCamada(request):

    return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):

    if request.GET["camada"]: #Si la camada existe.
        
        camada = request.GET["camada"] #Almacenar el número que estoy buscando (el número ingresado).
        cursos = Curso.objects.filter(camada__icontains=camada) #Vamos a decir que los nùmeros que están en la base de datos coincide con el número que pusimos nosotros (buscando un curso).
        cursos = Curso.objects.filter(camada__iexact=camada) #icontains significa que el número que buscamos está contenido en la camada.

        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos":cursos, "camada": camada})
    
    else:

        respuesta = "No enviaste datos."     

    return HttpResponse(respuesta)
