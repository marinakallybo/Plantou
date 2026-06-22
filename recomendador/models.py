from django.db import models


class Cultura(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    temperatura_minima = models.FloatField()
    temperatura_maxima = models.FloatField()
    solo_ideal = models.CharField(max_length=100)
    umidade_ideal = models.CharField(max_length=50)
    epoca_plantio = models.CharField(max_length=100)
    tempo_colheita_dias = models.IntegerField()
    dificuldade = models.CharField(max_length=50)

    def __str__(self):
        return self.nome