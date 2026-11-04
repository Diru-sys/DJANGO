from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido1 = models.CharField(max_length=20)
    apellido2 = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido1} {self.apellido2}"


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    cuerpo = models.TextField()
    fecha_publicacion = models.DateTimeField()

    def __str__(self):
        return f"{self.titulo}"