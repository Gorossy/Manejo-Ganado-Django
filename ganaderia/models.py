from django.db import models
from django.db.models.fields.mixins import FieldCacheMixin

'''class Veterinario(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
class Animal(models.Model):
    id = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=20)
    tipo = models.IntegerField()
    peso = models.IntegerField()
class Enfermedad(models.Model):
    id_animal = models.ForeignKey(Animal.id)
    nombre = models.CharField(max_length=20)
    id_veterinario = models.models.ForeignKey(Veterinario.id)
class Vacuna(models.Model):
    nombre = models.CharField(max_length=20)
    id_animal = models.ForeignKey(Animal.id)
    fecha = models.DateTimeField()
    id_veterinario = models.models.ForeignKey(Veterinario.id)
class Pajilla(models.Model):
    id = models.IntegerField(primary_key=True)
    id_animal = models.ForeignKey(Animal.id)
    fecha = models.DateTimeField()
    estado = models.IntegerField()
class Inseminacion(models.Model):
    id_animal = models.ForeignKey(Animal.id)
    id_pajilla = models.ForeignKey(Pajilla.id)
    evolucion = models.TextField(max_length=200)
    fecha = models.DateTimeField()
    id_veterinario = models.models.ForeignKey(Veterinario.id)
class Registro_mensual(models.Model):
    id_animal = models.ForeignKey(Animal.id)
    mes = models.IntegerField()
    evolucion = models.TextField(max_length=200)
class Baja(models.Model):
    id_animal = models.ForeignKey(Animal.id)
    motivo = models.TextField(max_length=200)
    fecha = models.DateTimeField()
class Nacido(models.Model):
    id = models.IntegerField(primary_key=True)
    id_animal = models.ForeignKey(Animal.id)
    sexo = models.IntegerField()
    fecha_destete = models.DateTimeField()
class Cliente(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
class Venta(models.Model):
    fecha = models.DateTimeField()
    id_cliente = models.ForeignKey(Cliente.id)
    precio = models.IntegerField()
class Alimentacion(models.Model):
    id_animal = models.ForeignKey(Animal.id)
    fecha = models.DateTimeField()
    kilos = models.IntegerField()
    consumo_agua = models.IntegerField()
class Leche(models.Model):
    id_animal = models.ForeignKey(Animal.id)
    fecha = models.DateTimeField()
'''