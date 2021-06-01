from typing import final
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.mixins import FieldCacheMixin

class Veterinario(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    tipo = models.CharField(max_length=10)
    def __str__(self):
        return self.nombre
class Animal(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    tipo = models.IntegerField()
    peso = models.IntegerField()
    def __str__(self):
        return str(self.id) 
class Enfermedadades(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    id_animal = models.ForeignKey(Animal,on_delete=CASCADE)
    id_veterinario = models.ForeignKey(Veterinario,on_delete=CASCADE)
    nombre = models.CharField(max_length=20)
    inicio = models.DateField()
    final = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.nombre
class Vacuna(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=20)
    id_animal = models.ForeignKey(Animal,on_delete=CASCADE)
    id_veterinario = models.ForeignKey(Veterinario,on_delete=CASCADE)
    fecha = models.DateField()
    def __str__(self):
        return self.nombre
class Cliente(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre
class Venta(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    fecha = models.DateField()
    tipo = models.IntegerField()
    id_producto = models.ForeignKey(Animal,on_delete=CASCADE)
    id_cliente = models.ForeignKey(Cliente,on_delete=CASCADE)
    precio = models.IntegerField()
    def __str__(self):
        return str(self.id)
class Pajilla(models.Model):
    id_animal = models.ForeignKey(Animal, on_delete=CASCADE)
    fecha = models.DateField()
    def __str__(self):
        return str(self.id_animal)
class VacaMadre(models.Model):
    id_animal = models.ForeignKey(Animal, on_delete=CASCADE)
    Embarazada = models.IntegerField()
    pajilla = models.ForeignKey(Pajilla, on_delete=CASCADE)
    fecha_inseminacion = models.DateField()
    id_veterinario = models.ForeignKey(Veterinario,on_delete=CASCADE)
    litros = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return str(self.id_animal)
class Evolucion(models.Model):
    id_animal = models.ForeignKey(Animal, on_delete=CASCADE)
    mes = models.DateField()
    descripcion = models.TextField()
    fecha_parto = models.DateTimeField(null=True, blank=True)
class Ternero(models.Model):
    id_animal = models.ForeignKey(Animal, on_delete=CASCADE)
    sexo = models.IntegerField()
    madre = models.ForeignKey(VacaMadre, on_delete=CASCADE,related_name='Madre')
    destete = models.DateField(null=True, blank=True)
    remplazo = models.IntegerField()
class Baja(models.Model):
    id_animal = models.ForeignKey(Animal, on_delete=CASCADE)
    motivo = models.IntegerField()
    fecha = models.DateField()
class Alimentacion(models.Model):
    id_animal = models.ForeignKey(Animal, on_delete=CASCADE)
    fecha = models.DateField()
    kilos = models.IntegerField()
    consumo_agua = models.IntegerField()