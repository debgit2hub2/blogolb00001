from django.db import models

# Create your models here.
class Asignatura(models.Model):
    curso = models.CharField(max_length=30)
    semestre = models.CharField(max_length=50)
    contenido = models.CharField(max_length=5000)

    def __str__(self):
        return self.curso

class Entrada(models.Model):
    curso = models.CharField(max_length=500)
    objetivo = models.TextField(max_length=5000)
    imagen = models.URLField()
    semestre = models.CharField(max_length=50)
    

    def __str__(self):
        return self.curso

class Comentario(models.Model):
    curso = models.CharField(max_length=500)
    Comentario = models.TextField(max_length=5000)

    def __str__(self):
        return self.curso