from django.db import models


class Programacion(models.Model):
    nombreEjercicio = models.CharField(null=False, max_length=200)
    ejercicio = models.TextField(null=False)
    puntaje = models.IntegerField(null=False, default=1)