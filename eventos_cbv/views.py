from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from eventos_cbv.models import Evento

class EventoLista(ListView):
    model = Evento

class EventoCrear(CreateView):
    model = Evento
    fields = ['titulo', 'descripcion', 'fecha', 'hora', 'duracion']
    success_url = reverse_lazy('eventos_cbv:lista_eventos_1')

class EventoEditar(UpdateView):
    model = Evento
    fields = ['titulo', 'descripcion', 'fecha', 'hora', 'duracion']
    success_url = reverse_lazy('eventos_cbv:lista_eventos_1')

class EventoBorrar(DeleteView):
    model = Evento
    success_url = reverse_lazy('eventos_cbv:lista_eventos_1')