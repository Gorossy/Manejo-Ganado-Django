from typing import final
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.mixins import FieldCacheMixin

class Veterinario(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    tipo = models.CharField(max_length=10)
class Animal(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    tipo = models.IntegerField()
    peso = models.IntegerField()
class Enfermedadades(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    id_animal = models.ForeignKey(Animal,on_delete=CASCADE)
    id_veterinario = models.ForeignKey(Veterinario,on_delete=CASCADE)
    nombre = models.CharField(max_length=20)
    inicio = models.DateTimeField(auto_now_add=True)
    final = models.DateTimeField(null=True, blank=True)
class Vacuna(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=20)
    id_animal = models.ForeignKey(Animal,on_delete=CASCADE)
    id_veterinario = models.ForeignKey(Veterinario,on_delete=CASCADE)
    fecha = models.DateTimeField()
class Cliente(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
class Venta(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    fecha = models.DateTimeField()
    tipo = models.IntegerField()
    id_venta = models.ForeignKey(Animal,on_delete=CASCADE)
    id_cliente = models.ForeignKey(Cliente,on_delete=CASCADE)
    precio = models.IntegerField()
class Pajilla(models.Model):
    id_animal = models.ForeignKey(Animal, on_delete=CASCADE)
    fecha = models.DateTimeField()
class VacaMadre(models.Model):
    id_animal = models.ForeignKey(Animal, on_delete=CASCADE)
    Embarazada = models.IntegerField()
    pajilla = models.ForeignKey(Pajilla, on_delete=CASCADE)
    fecha_inseminacion = models.DateTimeField()
    id_veterinario = models.ForeignKey(Veterinario,on_delete=CASCADE)
    litros = models.IntegerField(null=True, blank=True)
class Evolucion(models.Model):
    id_animal = models.ForeignKey(Animal, on_delete=CASCADE)
    mes = models.DateTimeField()
    descripcion = models.TextField()
    fecha_parto = models.DateTimeField()
class Ternero(models.Model):
    id_animal = models.ForeignKey(Animal, on_delete=CASCADE)
    sexo = models.IntegerField()
    madre = models.ForeignKey(Animal, on_delete=CASCADE,related_name='Madre')
    destete = models.DateTimeField()
    remplazo = models.IntegerField()
class Baja(models.Model):
    id_animal = models.ForeignKey(Animal, on_delete=CASCADE)
    motivo = models.IntegerField()
    fecha = models.DateTimeField()
class Alimentacion(models.Model):
    id_animal = models.ForeignKey(Animal, on_delete=CASCADE)
    fecha = models.DateTimeField()
    kilos = models.IntegerField()
    consumo_agua = models.IntegerField()