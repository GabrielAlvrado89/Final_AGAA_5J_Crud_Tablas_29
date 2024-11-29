from django.db import models

class Proveedores(models.Model):
    id_proveedores=models.IntegerField()
    Producto=models.CharField(max_length=100)
    Cantidad=models.CharField(max_length=100)
    Sucursal=models.CharField(max_length=100)
    Telefono=models.IntegerField()
    correo=models.CharField(max_length=100)
    Hora=models.CharField(max_length=100)
    FechaVenta=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre