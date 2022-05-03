from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    duracion = models.IntegerField(default=0)

    def __str__(self):
        txt="{0} - {1}"
        return txt.format(self.camada, self.nombre)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30, default="")
    email = models.EmailField(default="")

    def __str__(self):
        txt="{0} - {1}"
        return txt.format(self.nombre, self.apellido)


class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()

class Certificaciones (models.Model):
    nombre = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=30)
    fecha = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Certificaciones"
        verbose_name_plural = "Certificaciones"