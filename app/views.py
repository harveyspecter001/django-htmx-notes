from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse
from .models import Tarea



# Create your views here.
class indexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "app/pages/index.html")

def inicio(request):
    return render(request, "app/pages/inicio.html")



def lista_tareas(request):
    tareas = Tarea.objects.all().order_by('-fecha_creacion')
    return render(request, 'app/pages/lista_tareas.html', {'tareas': tareas})

def agregar_tarea(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        if titulo:
            Tarea.objects.create(titulo=titulo)
            tareas = Tarea.objects.all().order_by('-fecha_creacion')
            return render(request, 'app/pages/lista_tareas_partial.html', {'tareas': tareas})
    return HttpResponse('')

def toggle_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.completada = not tarea.completada
    tarea.save()
    
    tareas = Tarea.objects.all().order_by('-fecha_creacion')
    return render(request, 'app/pages/lista_tareas_partial.html', {'tareas': tareas})

def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.delete()
    
    tareas = Tarea.objects.all().order_by('-fecha_creacion')
    return render(request, 'app/pages/lista_tareas_partial.html', {'tareas': tareas})