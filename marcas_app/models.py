from django.db import models

class marcas(models.Model):
    id_marcas=models.IntegerField()
    id_sucursal=models.IntegerField()
    id_producto=models.IntegerField()
    Nombre_Marca=models.CharField(max_length=100)
    Numtelefono=models.IntegerField()
    Correo=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre