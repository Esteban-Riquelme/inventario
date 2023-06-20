from django.db import models

    
class Categoria(models.Model):
    nombre = models.CharField(max_length=10)
    def __str__(self):
        return self.nombre

class Dispositivo(models.Model):
    serial= models.CharField(max_length=15,primary_key=True)
    marca = models.CharField(max_length=15)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.serial

class Area(models.Model):
    area_especifica= models.CharField(max_length=20)
    def __str__(self):
        return self.area_especifica


class Ubicacion(models.Model):
    piso = models.CharField(max_length=15)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.piso}  {self.area}"

class Detalle(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    estado = models

    def __str__(self):
        return f"{self.dispositivo}    {self.estado}"
