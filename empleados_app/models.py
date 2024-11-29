from django.db import models

class empleados(models.Model):
    id_empleado=models.IntegerField()
    Nombre_Completo=models.CharField(max_length=100)
    numtelefono=models.IntegerField()
    CURP=models.CharField(max_length=100)
    RFC=models.CharField(max_length=100)
    Edad=models.IntegerField()
    sexo=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre