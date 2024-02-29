from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100, )
    idade = models.IntegerField()
    remedios = models.TextField(max_length=5000, )

    def __str__(self):
        return self.nome