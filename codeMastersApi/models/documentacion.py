from django.db import models


class Documentacion(models.Model):
    nombreLeccion = models.CharField(null=False, max_length=200)
    documentacion = models.TextField(null=False)
    preguntaQuizz = models.CharField(null=False, max_length=200)
    respuestaCorrecta = models.CharField(null=False, max_length=200)
    respuestaIncorrecta1 = models.CharField(null=False, max_length=200)
    respuestaIncorrecta2 = models.CharField(null=False, max_length=200)
    respuestaIncorrecta3 = models.CharField(null=False, max_length=200)
    puntaje = models.IntegerField(null=False, default=1)
