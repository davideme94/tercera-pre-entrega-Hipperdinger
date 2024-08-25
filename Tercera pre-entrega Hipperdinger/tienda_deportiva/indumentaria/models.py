from django.db import models

class Camiseta(models.Model):
    name = models.CharField(max_length=50)
    talle = models.CharField(max_length=3)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Short(models.Model):
    name = models.CharField(max_length=50)
    talle = models.CharField(max_length=3)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Botin(models.Model):
    name = models.CharField(max_length=50)
    talle = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name

    
