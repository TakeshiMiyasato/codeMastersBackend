from django.contrib.auth.models import User
from django.db import models


class PuntosPorJugador(models.Model):
    idJugador = models.ForeignKey(User, on_delete=models.CASCADE)
    puntajeAnual = models.IntegerField(null=False, default=0)
    puntajeTotal = models.IntegerField(null=False, default=0)
    nivel = models.IntegerField(null=False, default=1)

    @property
    def user_name(self):
        return self.idJugador.get_username()