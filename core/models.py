from django.db import models

# Create your models here.

class Cursos(models.Model):
    id_curso = models.AutoField(primary_key=True)
    titulo_curso = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    qtt_modulos = models.PositiveIntegerField()
    categoria = models.CharField(max_length=100)
    avaliacao = models.DecimalField(max_digits=3, decimal_places=2)
    instrutor = models.CharField(max_length=255)
    plataforma = models.CharField(max_length=100)

    class Meta:
        db_table = 'Cursos'

    def __str__(self):
        return self.titulo_curso