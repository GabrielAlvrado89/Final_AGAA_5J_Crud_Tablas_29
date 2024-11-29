from django.db import models

class Productos(models.Model):
    id_producto=models.IntegerField()
    id_proveedores=models.IntegerField()
    id_sucursal=models.IntegerField()
    TipoProducto=models.CharField(max_length=100)
    Cantidad=models.CharField(max_length=100)
    NombreProducto=models.CharField(max_length=100)
    Sucursal=models.CharField(max_length=100)
    Correo=models.CharField(max_length=100)
    NumTelefono=models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    
    def __str__(self):
        return self.nombre