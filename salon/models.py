from django.db import models


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    duracion = models.CharField(max_length=50)

    def _str_(self):
        return self.nombre


class Estilista(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='estilistas/', blank=True, null=True)

    def _str_(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    existencias = models.PositiveIntegerField()

    def _str_(self):
        return self.nombre


class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    horario = models.CharField(max_length=100)

    def _str_(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    fecha_registro = models.DateField(auto_now_add=True)

    def _str_(self):
        return self.nombre
    
