from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields }
class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'
class VeterinarioForm(forms.ModelForm):
    class Meta:
        model = Veterinario
        fields = '__all__'
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
class EnfermedadadesForm(forms.ModelForm):
    class Meta:
        model = Enfermedadades
        fields = '__all__'

class VacunaForm(forms.ModelForm):
    class Meta:
        model = Vacuna
        fields = '__all__'
class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'
class EvolucionForm(forms.ModelForm):
    class Meta:
        model = Evolucion
        fields = '__all__'

class TerneroForm(forms.ModelForm):
    class Meta:
        model = Ternero
        fields = '__all__'

class BajaForm(forms.ModelForm):
    class Meta:
        model = Baja
        fields = '__all__'

class AlimentacionForm(forms.ModelForm):
    class Meta:
        model = Alimentacion
        fields = '__all__'
class PajillaForm(forms.ModelForm):
    class Meta:
        model = Pajilla
        fields = '__all__'
class VacaMadreForm(forms.ModelForm):
    class Meta:
        model = VacaMadre
        fields = '__all__'




