from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static

from . import views

urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    path('agregar/', views.agregar_tarea, name='agregar_tarea'),
    path('toggle/<int:tarea_id>/', views.toggle_tarea, name='toggle_tarea'),
    path('eliminar/<int:tarea_id>/', views.eliminar_tarea, name='eliminar_tarea'),
    #path("",views.indexView.as_view(), name="index"),
    path("inicio",views.inicio, name="inicio"),




    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)