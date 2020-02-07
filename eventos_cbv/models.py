from django.db import models
from django.urls import reverse
import datetime

class Evento(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    fecha = models.DateField("Date", default=datetime.date.today)
    hora = models.IntegerField(default=8)
    duracion = models.IntegerField(default=1)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('eventos_cbv:editar_evento', kwargs={'pk': self.pk})