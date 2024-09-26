from django.db import models

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    periodo = models.IntegerField()
    dependencias = models.ManyToManyField('self', symmetrical=False, blank=True)
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

