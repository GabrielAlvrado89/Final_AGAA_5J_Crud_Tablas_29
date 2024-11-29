from django.db import models

class clientes(models.Model):
    id_cliente=models.IntegerField()
    NombreCompleto=models.CharField(max_length=100)
    Edad = models.IntegerField(default=0)
    NumeroTelefono = models.IntegerField(default=0)
    Correo=models.CharField(max_length=100)
    Domicilio=models.CharField(max_length=100)
    FormaPago = models.CharField(max_length=50, default="Efectivo")
    
    def __str__(self):
        return self.nombre