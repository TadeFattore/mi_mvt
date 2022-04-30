from django.db import models

# Create your models here.
class Familiares(models.Model):
    edad=models.IntegerField()
    nombre=models.CharField(max_length=30)
    fechaDeNac=models.DateField()

class Abuelos(models.Model):
    nombre=models.CharField(max_length=30)
    paisDeNac=models.CharField(max_length=30)
    anioDeNac=models.IntegerField()

    def __str__(self):
        txt="{0} - {1}"
        return txt.format(self.nombre,self.anioDeNac)

class Padres(models.Model):
    nombre=models.CharField(max_length=30)
    paisDeNac=models.CharField(max_length=30)
    anioDeNac=models.IntegerField()

    def __str__(self):
        txt='{0} , {1}'
        return txt.format(self.nombre,self.anioDeNac)

class Hermanos(models.Model):
    nombre=models.CharField(max_length=30)
    paisDeNac=models.CharField(max_length=30)
    anioDeNac=models.IntegerField()