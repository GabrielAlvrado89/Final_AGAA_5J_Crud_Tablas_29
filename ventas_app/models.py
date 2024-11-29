from django.db import models

class ventas(models.Model):
    id_venta=models.IntegerField()
    id_Productos=models.IntegerField()
    id_Clientes=models.IntegerField()
    Cantidad=models.CharField(max_length=100)
    Hora_venta=models.CharField(max_length=4)
    Sucursal=models.CharField(max_length=100)
    Marcas=models.CharField(max_length=100)
    FormaPago = models.CharField(max_length=50, default="Efectivo")
    
    def __str__(self):
        return self.nombre
