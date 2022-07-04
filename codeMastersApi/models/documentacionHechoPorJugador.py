from django.db import models
from django.contrib.auth.models import User

from codeMastersApi.models import Documentacion


class DocumentacionHechoPorJugador(models.Model):
    usuarioId = models.ForeignKey(User, on_delete=models.CASCADE)
    documentacionId = models.ForeignKey(Documentacion, on_delete=models.CASCADE)
