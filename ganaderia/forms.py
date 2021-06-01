from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.enums import Choices
from django.db.models.fields import IntegerField
from django.forms import widgets
from .models import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields }
class dateinput(forms.DateTimeInput):
    format='%d/%m/%Y'
    input_type = 'date'

Embarazo =(
    (1, "Si"),
    (0, "No"),
)
tipo=(
    ('Persona','Persona'),
    ('Empresa','Empresa')
)
tipo2 =(
    (0, "Ternero"),
    (1, "Toro"),
    (2, "Vaca"),
    (3, "Cebo")
)
tipoventa =(
    (0, "Pajilla"),
    (1, "Carne"),
)
reemplazo =(
    (1, "Si"),
    (2, "No"),
)
sexo =(
    (1, "Macho"),
    (0, "Hembra"),
)
motivo =(
    (0, "Venta"),(1, "Sacrificio"),(2, "Enfermedad"),
)

class AnimalForm(forms.ModelForm):
    tipo = forms.ChoiceField(choices=tipo2)
    class Meta:
        model = Animal
        fields = '__all__'
class VeterinarioForm(forms.ModelForm):
    tipo = forms.ChoiceField(choices=tipo)
    class Meta:
        model = Veterinario
        fields = ['id','nombre','telefono','tipo']
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
class EnfermedadadesForm(forms.ModelForm):
    class Meta:
        model = Enfermedadades
        fields = ['id','id_animal','id_veterinario','nombre','inicio','final']
        widgets = {'inicio':dateinput,'final':dateinput}
        widgets = {'inicio': forms.TextInput(
        attrs={'type': 'date'}),'final': forms.TextInput(
        attrs={'type': 'date'}),}


class VacunaForm(forms.ModelForm):
    class Meta:
        model = Vacuna
        fields = ['id','nombre','id_animal','id_veterinario','fecha']
        widgets = {'fecha': forms.TextInput(
        attrs={'type': 'date'}),}
        
class VentaForm(forms.ModelForm):
    tipo = forms.ChoiceField(choices=tipoventa)
    class Meta:
        model = Venta
        fields = ['id','fecha','tipo','id_producto','id_cliente','precio']
        widgets = {'fecha': forms.TextInput(
        attrs={'type': 'date'}),}
class EvolucionForm(forms.ModelForm):
    class Meta:
        model = Evolucion
        fields = ['id_animal','mes','descripcion','fecha_parto']
        widgets = {'mes': forms.TextInput(
        attrs={'type': 'date'}),'fecha_parto': forms.TextInput(
        attrs={'type': 'date'}),}

class TerneroForm(forms.ModelForm):
    remplazo = forms.ChoiceField( choices=reemplazo)
    sexo = forms.ChoiceField(choices=sexo)
    class Meta:
        model = Ternero
        fields = ['id_animal','sexo','madre','destete','remplazo']
        widgets = {'destete': forms.TextInput(
        attrs={'type': 'date'}),}

class BajaForm(forms.ModelForm):
    motivo = forms.ChoiceField(choices=motivo)
    class Meta:
        model = Baja
        fields = ['id_animal','motivo','fecha']
        widgets = {'fecha': forms.TextInput(
        attrs={'type': 'date'}),}

class AlimentacionForm(forms.ModelForm):
    class Meta:
        model = Alimentacion
        fields = ['id_animal','fecha','kilos','consumo_agua']
        widgets = {'fecha': forms.TextInput(
        attrs={'type': 'date'}),}
class PajillaForm(forms.ModelForm):
    class Meta:
        model = Pajilla
        fields = ['id_animal','fecha']
        widgets = {'fecha': forms.TextInput(
        attrs={'type': 'date'}),}
class VacaMadreForm(forms.ModelForm):
    Embarazada = forms.ChoiceField(choices = Embarazo)
    class Meta:
        model = VacaMadre
        fields = ['id_animal','Embarazada','pajilla','fecha_inseminacion','id_veterinario','litros']
        widgets = {'fecha_inseminacion': forms.TextInput(
        attrs={'type': 'date'}),
}




