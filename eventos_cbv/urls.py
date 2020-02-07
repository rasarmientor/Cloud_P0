from django.urls import path

from . import views

app_name = 'eventos_cbv'

urlpatterns = [
  path('', views.EventoLista.as_view(), name='lista_eventos_1'),
  path('new', views.EventoCrear.as_view(), name='nuevo_evento'),
  path('edit/<int:pk>', views.EventoEditar.as_view(), name='editar_evento'),
  path('delete/<int:pk>', views.EventoBorrar.as_view(), name='borrar_evento'),
]