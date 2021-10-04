from django.forms.forms import Form
from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from .forms import *
from .models import *
from django.template import RequestContext

# Create your views here.
def inicio(request):
    conteo = Venta.objects.count()
    conteo2 = Animal.objects.count()
    conteo3 = Veterinario.objects.count()
    context = {'conteo': conteo, 'conteo2': conteo2, 'conteo3': conteo3}
    if request.user.is_authenticated:
        return render(request, 'menu.html', context)
    else:
       return render(request, 'index.html', context)
def productos(request):
     return render(request, 'portfolio-2-column.html')
def contacto(request):
    return render(request, 'contact.html')
def nosotros(request):
    return render(request, 'pages-about-us.html')
def registrarse(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            return redirect('index')
        else:
            print("Formulario no valido")
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request,'pages-sign-up.html', context)
def crearAnimal(request):
    if request.method =='GET':
        form = AnimalForm()
        contexto = {
        'form':form
        }
    else:
        form = AnimalForm(request.POST)
        contexto = {
        'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'animales.html', contexto)


def mostraranimal1(request):
    animal = Animal.objects.filter(tipo = 1)
    contexto = {
        'formulario':animal,
        }
    return render(request,'mostrar_animales.html',contexto)
def mostraranimal2(request):
    animal = Animal.objects.filter(tipo = 2)
    contexto = {
        'formulario':animal,
        }
    return render(request,'mostrar_animales.html',contexto)
def mostraranimal3(request):
    animal = Animal.objects.filter(tipo = 0)
    contexto = {
        'formulario':animal,
        }
    return render(request,'mostrar_animales.html',contexto)
def detallestoro(request, id):
    enfermedad = Enfermedadades.objects.filter(id_animal = id)
    vacuna = Vacuna.objects.filter(id_animal = id)
    alimentacion = Alimentacion.objects.filter(id_animal = id)
    baja = Baja.objects.filter(id_animal = id)
    contexto = {
        'enfermedad':enfermedad,'vacuna':vacuna,'alimentacion':alimentacion,'baja':baja
        }
    return render(request,'detalles.html',contexto)
def detallesvaca(request, id):
    enfermedad = Enfermedadades.objects.filter(id_animal = id)
    vacuna = Vacuna.objects.filter(id_animal = id)
    alimentacion = Alimentacion.objects.filter(id_animal = id)

    baja = Baja.objects.filter(id = id)
    madre = VacaMadre.objects.filter(id_animal = id)
    evolucion = Evolucion.objects.filter(id_animal =id)
    contexto = {
        'enfermedad':enfermedad,'vacuna':vacuna,'alimentacion':alimentacion,'baja':baja, 'madre':madre,'evolucion':evolucion,
        }
    return render(request,'detalles2.html',contexto)
def detallesternero(request, id):
    enfermedad = Enfermedadades.objects.filter(id_animal = id)
    vacuna = Vacuna.objects.filter(id_animal = id)
    alimentacion = Alimentacion.objects.filter(id_animal = id)
    baja = Baja.objects.filter(id = id)
    ternero = Ternero.objects.filter(id_animal = id)
    vacaMadre = VacaMadre.objects.all()
    contexto = {
        'enfermedad':enfermedad,'vacuna':vacuna,'alimentacion':alimentacion,'baja':baja,'ternero':ternero,'vacaMadre':vacaMadre
        }
    return render(request,'detalles3.html',contexto)
def mostrarveterinario(request):
    animal = Veterinario.objects.all()
    contexto = {
        'formulario':animal,
        }
    return render(request,'mostrar_veterinario.html',contexto)
def mostrarenfermedades(request):
    animal = Enfermedadades.objects.all()
    contexto = {
        'formulario':animal,
        }
    return render(request,'mostrar_enfermedades.html',contexto)
def mostrarvacuna(request):
    animal = Vacuna.objects.all()
    contexto = {
        'formulario':animal,
        }
    return render(request,'mostrar_vacuna.html',contexto)
def mostrarcliente(request):
    animal = Cliente.objects.all()
    contexto = {
        'formulario':animal,
        }
    return render(request,'mostrar_cliente.html',contexto)
def mostrarventa(request):
    venta = Venta.objects.all()
    animalito = Animal.objects.all()
    contexto = {
        'formulario':venta, 'animalito':animalito,
        }
    return render(request,'mostrar_venta.html',contexto)
def mostrarpajilla(request):
    animal = Pajilla.objects.all()
    contexto = {
        'formulario':animal,
        }
    return render(request,'mostrar_pajilla.html',contexto)
def mostrarvacamadre(request):
    animal = VacaMadre.objects.all()
    contexto = {
        'formulario':animal,
        }
    return render(request,'mostrar_vacamadre.html',contexto)
def mostrarevolucion(request):
    animal = Evolucion.objects.all()
    contexto = {
        'formulario':animal,
        }
    return render(request,'mostrar_evolucion.html',contexto)
def mostrarternero(request):
    animal = Ternero.objects.all()
    contexto = {
        'formulario':animal,
        }
    return render(request,'mostrar_ternero.html',contexto)
def mostrarbaja(request):
    animal = Baja.objects.all()
    contexto = {
        'formulario':animal,
        }
    return render(request,'mostrar_baja.html',contexto)
def mostraralimentacion(request):
    animal = Alimentacion.objects.all()
    contexto = {
        'formulario':animal,
        }
    return render(request,'mostrar_alimentacion.html',contexto)

def crearVeterinario(request):
    if request.method =='GET':
        form = VeterinarioForm()
        contexto = {
        'form':form
        }
    else:
        form = VeterinarioForm(request.POST)
        contexto = {
        'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('mostrarveterinario')
    return render(request,'animales.html', contexto)
def crearCliente(request):
    if request.method =='GET':
        form = ClienteForm()
        contexto = {
        'form':form
        }
    else:
        form = ClienteForm(request.POST)
        contexto = {
        'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('mostrarcliente')
    return render(request,'animales.html', contexto)
def crearEnfermedad(request):
    if request.method =='GET':
        form = EnfermedadadesForm()
        contexto = {
        'form':form
        }
    else:
        form = EnfermedadadesForm(request.POST)
        contexto = {
        'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('mostrarenfermedades')
    return render(request,'animales.html', contexto)
def crearVacuna(request):
    if request.method =='GET':
        form = VacunaForm()
        contexto = {
        'form':form
        }
    else:
        form = VacunaForm(request.POST)
        contexto = {
        'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('mostrarvacuna')
    return render(request,'animales.html', contexto)
def crearVenta(request):
    if request.method =='GET':
        form = VentaForm()
        contexto = {
        'form':form
        }
    else:
        form = VentaForm(request.POST)
        contexto = {
        'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('mostrarventa')
    return render(request,'animales.html', contexto)
def crearEvolucion(request):
    if request.method =='GET':
        form = EvolucionForm()
        contexto = {
        'form':form
        }
    else:
        form = EvolucionForm(request.POST)
        contexto = {
        'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('mostrarevolucion')
    return render(request,'animales.html', contexto)
def crearTernero(request):
    if request.method =='GET':
        form = TerneroForm()
        contexto = {
        'form':form
        }
    else:
        form = TerneroForm(request.POST)
        contexto = {
        'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('mostrarternero')
    return render(request,'animales.html', contexto)
def crearBaja(request):
    if request.method =='GET':
        form = BajaForm()
        contexto = {
        'form':form
        }
    else:
        form = BajaForm(request.POST)
        contexto = {
        'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('mostrarbaja')
    return render(request,'animales.html', contexto)
def crearPajilla(request):
    if request.method =='GET':
        form = PajillaForm()
        contexto = {
        'form':form
        }
    else:
        form = PajillaForm(request.POST)
        contexto = {
        'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('mostrarpajilla')
    return render(request,'animales.html', contexto)
def crearAlimentacion(request):
    if request.method =='GET':
        form = AlimentacionForm()
        contexto = {
        'form':form
        }
    else:
        form = AlimentacionForm(request.POST)
        contexto = {
        'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('mostraralimentacion')
    return render(request,'animales.html', contexto)
def crearVacaMadre(request):
    if request.method =='GET':
        form = VacaMadreForm()
        contexto = {
        'form':form
        }
    else:
        form = VacaMadreForm(request.POST)
        contexto = {
        'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('mostrarvacamadre')
    return render(request,'animales.html', contexto)

def editarAnimal(request,id):
    animal = Animal.objects.get(id = id)
    form = AnimalForm(instance=animal)
    if request.method =='POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('index')
    contexto = {'form':form}
    return render(request,'animales.html',contexto)

def editarVeterinario(request,id):
    veterinario = Veterinario.objects.get(id = id)
    form = VeterinarioForm(instance=veterinario)
    if request.method =='POST':
        form = VeterinarioForm(request.POST, instance=veterinario)
        if form.is_valid():
            form.save()
            return redirect('mostrarveterinario')
    contexto = {'form':form}
    return render(request,'animales.html',contexto)

def editarCliente(request,id):
    cliente = Cliente.objects.get(id = id)
    form = ClienteForm(instance=cliente)
    if request.method =='POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('mostrarcliente')
    contexto = {'form':form}
    return render(request,'animales.html',contexto)
def editarEnfermedadades(request,id):
    enfermedadades = Enfermedadades.objects.get(id = id)
    form = EnfermedadadesForm(instance=enfermedadades)
    if request.method =='POST':
        form = EnfermedadadesForm(request.POST, instance=enfermedadades)
        if form.is_valid():
            form.save()
            return redirect('mostrarenfermedades')
    contexto = {'form':form}
    return render(request,'animales.html',contexto)
def editarVacuna(request,id):
    vacuna = Vacuna.objects.get(id = id)
    form = VacunaForm(instance=vacuna)
    if request.method =='POST':
        form = VacunaForm(request.POST, instance=vacuna)
        if form.is_valid():
            form.save()
            return redirect('mostrarvacuna')
    contexto = {'form':form}
    return render(request,'animales.html',contexto)
def editarVenta(request,id):
    venta = Venta.objects.get(id = id)
    form = VentaForm(instance=venta)
    if request.method =='POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('mostrarventa')
    contexto = {'form':form}
    return render(request,'animales.html',contexto)
def editarPajilla(request,id):
    pajilla = Pajilla.objects.get(id = id)
    form = PajillaForm(instance=pajilla)
    if request.method =='POST':
        form = PajillaForm(request.POST, instance=pajilla)
        if form.is_valid():
            form.save()
            return redirect('mostrarpajilla')
    contexto = {'form':form}
    return render(request,'animales.html',contexto)
def editarVacaMadre(request,id):
    vacaMadre = VacaMadre.objects.get(id = id)
    form = VacaMadreForm(instance=vacaMadre)
    if request.method =='POST':
        form = VacaMadreForm(request.POST, instance=vacaMadre)
        if form.is_valid():
            form.save()
            return redirect('mostrarvacamadre')
    contexto = {'form':form}
    return render(request,'animales.html',contexto)
def editarEvolucion(request,id):
    evolucion = Evolucion.objects.get(id = id)
    form = EvolucionForm(instance=evolucion)
    if request.method =='POST':
        form = EvolucionForm(request.POST, instance=evolucion)
        if form.is_valid():
            form.save()
            return redirect('mostrarevolucion')
    contexto = {'form':form}
    return render(request,'animales.html',contexto)
def editarTernero(request,id):
    ternero = Ternero.objects.get(id = id)
    form = TerneroForm(instance=ternero)
    if request.method =='POST':
        form = TerneroForm(request.POST, instance=ternero)
        if form.is_valid():
            form.save()
            return redirect('mostrarternero')
    contexto = {'form':form}
    return render(request,'animales.html',contexto)
def editarBaja(request,id):
    baja = Baja.objects.get(id = id)
    form = BajaForm(instance=baja)
    if request.method =='POST':
        form = BajaForm(request.POST, instance=baja)
        if form.is_valid():
            form.save()
            return redirect('mostrarbaja')
    contexto = {'form':form}
    return render(request,'animales.html',contexto)
def editarAlimentacion(request,id):
    alimentacion = Alimentacion.objects.get(id = id)
    form = AlimentacionForm(instance=alimentacion)
    if request.method =='POST':
        form = AlimentacionForm(request.POST, instance=alimentacion)
        if form.is_valid():
            form.save()
            return redirect('mostraralimentacion')
    contexto = {'form':form}
    return render(request,'animales.html',contexto)
def eliminarVeterinario(request, id):
    variable = Veterinario.objects.get(id = id)
    variable.delete()
    return redirect("mostrarveterinario")
def eliminarAnimal(request, id):
    variable = Animal.objects.get(id = id)
    variable.delete()
    return redirect("index")
def eliminarEnfermedadades(request, id):
    variable = Enfermedadades.objects.get(id = id)
    variable.delete()
    return redirect("mostrarenfermedades")
def eliminarVacuna(request, id):
    variable = Vacuna.objects.get(id = id)
    variable.delete()
    return redirect("mostrarvacuna")
def eliminarCliente(request, id):
    variable = Cliente.objects.get(id = id)
    variable.delete()
    return redirect("mostrarcliente")
def eliminarVenta(request, id):
    variable = Venta.objects.get(id = id)
    variable.delete()
    return redirect("mostrarventa")
def eliminarPajilla(request, id):
    variable = Pajilla.objects.get(id = id)
    variable.delete()
    return redirect("mostrarpajilla")
def eliminarVacaMadre(request, id):
    variable = VacaMadre.objects.get(id = id)
    variable.delete()
    return redirect("mostrarvacamadre")
def eliminarEvolucion(request, id):
    variable = Evolucion.objects.get(id = id)
    variable.delete()
    return redirect("mostrarevolucion")
def eliminarTernero(request, id):
    variable = Ternero.objects.get(id = id)
    variable.delete()
    return redirect("mostrarternero")
def eliminarBaja(request, id):
    variable = Baja.objects.get(id = id)
    variable.delete()
    return redirect("mostrarbaja")
def eliminarAlimentacion(request, id):
    variable = Alimentacion.objects.get(id = id)
    variable.delete()
    return redirect("mostraralimentacion")
