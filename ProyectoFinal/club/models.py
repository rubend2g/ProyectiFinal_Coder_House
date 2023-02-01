from django.db import models

class Actividad(models.Model):
    nombre = models.CharField(max_length=30)
    actividad = models.CharField(max_length=30)
    
class Natacion(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=30)
    actividad = models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - DNI {self.dni} - Actividad {self.actividad}"

class Gimnasio(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=30)
    actividad = models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - DNI {self.dni} - Actividad {self.actividad}"
class Futbol(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=30)
    actividad = models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - DNI {self.dni} - Actividad {self.actividad}"