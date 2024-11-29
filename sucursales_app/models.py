from django.db import models

# Create your models here.
class sucursales(models.Model):
    id_sucursal=models.IntegerField()
    nombre=models.CharField(max_length=100)
    Direccion=models.CharField(primary_key=True,max_length=6)
    NumTelefono=models.IntegerField()
    correo=models.CharField(max_length=100)
    Horario=models.CharField(max_length=4)
    
    def __str__(self):
        return self.nombre