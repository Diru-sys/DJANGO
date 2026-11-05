from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='posts')
    cuerpo = models.TextField()
    fecha_publicacion = models.DateTimeField()

    def __str__(self):
        return f"{self.titulo}"