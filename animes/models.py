from django.db import models
from django.contrib.auth.models import User


class Anime(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_anime = models.CharField(max_length=200)
    n_eps = models.CharField(max_length=10000)
    eps_assistidos = models.CharField(max_length=10000)
    estado = models.CharField(max_length=100)
    nota = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True, null=True)

    def __str__(self):
        return self.nome_anime

