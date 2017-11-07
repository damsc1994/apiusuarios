from django.db import models

# Create your models here.

class Personas(models.Model):
    nombres = models.TextField(max_length=20)
    apellidos = models.TextField(max_length=20)
    edad = models.IntegerField()
    direccion = models.TextField(max_length=100)


    def __str__(self):
        return "%s %s" % (self.nombres, self.apellidos)

class Usuarios(models.Model):
    nombre_usuario = models.TextField(max_length=10, unique=True)
    correo = models.EmailField(max_length=50)
    contrasena = models.TextField(max_length=100)
    persona = models.ForeignKey(
        'Personas',
        related_name = 'persona',
        on_delete = models.CASCADE,
        null=False,
        )
