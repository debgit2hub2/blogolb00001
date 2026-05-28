from django.shortcuts import render
from artezt0003.models import Entrada, Comentario, Asignatura
from artezt0003.forms import ComentarioForm
from django.core.mail import send_mail

# Create your views here.
def home(request):
    articulos = Entrada.objects.all()
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            curso = form.cleaned_data['curso']
            comentario = form.cleaned_data['comentario']
            obj = Comentario(curso=curso, Comentario=comentario)
            obj.save()
             
            #configuración del correo
            asunto = form.cleaned_data["asignatura"] 
            comentario = form.cleaned_data["comentario"]
            direccion = "dgjangobackend@gmail.com"
            destinatario = ["fortreme.43@gmail.com"]

            send_mail(asunto,comentario,direccion,destinatario)

            form = ComentarioForm() 
            comentario = "Gracias por su comentario"
            return render(request,"introautomabigdata.html",{"articulos":articulos,"comentario": comentario,"form":form})
    form = ComentarioForm()    
    return render(request,"introautomabigdata.html",{"articulos": articulos,"form":form})

def consultar(request):
    asignatura = Asignatura.objects.all()
    return render(request,'Semestre1.html',{
        'asignatura' : asignatura
        })

def guardar(request):
    curso = request.POST["curso"]
    semestre = request.POST["semestre"]
    contenido = request.POST["contenido"]
    p = Asignatura(curso=curso,semestre=semestre,contenido=contenido )
    p.save()
    messages.success(request, 'Asignatura agregada')
    return redirect('consultar') 
         
def eliminar(request,id):
    asignatura = Asignatura.objects.filter(pk=id)
    asignatura.delete()
    messages.success(request,"Asignatura eliminada")
    return redirect('consultar')

def detalle(request,id):
    asignatura = Asignatura.objects.get(pk=id)
    return render(request,"asignaturaEditar.html",{
        "asignatura" : asignatura 
    })

def editar(request):
    curso = request.POST["curso"]
    semestre = request.POST["semestre"]
    contenido = request.POST["contenido"]
    id = request.POST["id"]
    Asignatura.objects.filter(pk=id).update(id=id,curso=curso,semestre=semestre,contenido=contenido)
    messages.success(request, 'Asignatura actualizadaada')
