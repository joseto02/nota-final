from django.db import models

# Create your models here.

opciones_consultas = [
    [0, "consultas"],
    [1, "reclamo"],
    [2, "sugerencias"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    
    def __str__(self):
        return self.nombre