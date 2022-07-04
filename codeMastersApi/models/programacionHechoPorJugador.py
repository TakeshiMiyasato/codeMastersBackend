from builtins import property

from django.contrib.auth.models import User
from django.db import models

from codeMastersApi.models.programacion import Programacion


class ProgramacionHechoPorJugador(models.Model):
    programacionId = models.ForeignKey(Programacion, on_delete=models.CASCADE)
    usuarioId = models.ForeignKey(User, on_delete=models.CASCADE)
    codigo = models.TextField(null=False)
    revisado = models.BooleanField(default=False)
    correcto = models.BooleanField(default=False)

    @property
    def user_name(self):
        return self.usuarioId.get_username()