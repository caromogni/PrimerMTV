from django.db import models

# Create your models here.

class Familiares(models.Model):
    nombre=models.CharField(max_length=30)
    edad=models.IntegerField(max_length=3)
    nacimiento=models.DateField()
    
    def __str__(self):
        return f'NOMBRE: {self.nombre} EDAD: {self.edad} FECHA DE NACIMIENTO: {self.nacimiento}'