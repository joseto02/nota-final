from django.db import models

# Create your models here.

class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20, blank= False, null=False)
    apellido_paterno = models.CharField(max_length=25)
    apellido_materno = models.CharField(max_length=25, null=False, blank=True)
    telefono = models.IntegerField(null=False)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.nombre) + " " + str(self.apellido_paterno)


# class Marca(models.Model):
#     id_marca = models.AutoField(primary_key=True)
#     nombre_marca = models.CharField(max_length=100)
    
#     def __str__(self):
#         return str(self.id_marca) + " " + str(self.nombre_marca)

# class Modelo_zapatilla(models.Model):
#     id_modelo = models.AutoField(primary_key=True)
#     nombre_modelo = models.CharField(max_length=100)

#     def __str__(self):
#         return str(self.id_modelo) + " " + str(self.nombre_modelo)


class Zapatilla(models.Model):
    id_zapatilla = models.AutoField(primary_key=True)
    precio = models.IntegerField()
    talla = models.IntegerField(null=True)
    stock = models.IntegerField(null=True)
    marca = models.CharField(max_length=20, null=False, blank=False, default="Sin especificar")
    modelo = models.CharField(max_length=100, null=False, blank=False, default="Sin especificar")

    def __str__(self):
        return str(self.id_zapatilla) + " " + str(self.marca) + " " + str(self.modelo) + " " + str(self.precio)


class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    fecha_compra = models.DateField(blank=True, null= False)
    id_zapatilla = models.ForeignKey(Zapatilla, on_delete=models.CASCADE, to_field="id_zapatilla")
    
    def __str__(self):
        return str(self.id_compra)+ " " + str(self.fecha_compra)

class DetalleCompra(models.Model):
    cant_unidades = models.IntegerField()
    sub_total = models.IntegerField()
    total = models.IntegerField()
    id_compra = models.ForeignKey(Compra, on_delete=models.CASCADE, to_field="id_compra")
    
    def __str__(self):
        return str(self.total)