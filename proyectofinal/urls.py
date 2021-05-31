"""proyectofinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ganaderia.views import *
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('', inicio, name='index'),
    path('admin/', admin.site.urls),
    path('registrarse/', registrarse, name='registro'),
    path('login/', LoginView.as_view(template_name='pages-login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('productos/', LoginView.as_view(template_name='portfolio-2-column.html'), name='productos'),
    path('contact/', LoginView.as_view(template_name='contact.html'), name='contact'),
    path('nosotros/', LoginView.as_view(template_name='pages-about-us.html'), name='nosotros'),
    
    path('crear_animal/', crearAnimal,name='crearAnimal'),
    path('animales/',mostraranimal,name='mostraranimal'),
    path('editaranimal/<int:id>/',editarAnimal,name='editarAnimal'),
    path('eliminaranimal/<int:id>/',eliminarAnimal,name='eliminarAnimal'),

    path('crear_veterinario/', crearVeterinario,name='crearveterinario'),
    path('veterinario/',mostrarveterinario,name='mostrarveterinario'),
    path('editarveterinario/<int:id>/',editarVeterinario,name='editarVeterinario'),
    path('eliminarveterinario/<int:id>/',eliminarVeterinario,name='eliminarVeterinario'),

    path('crear_enfermedades/', crearEnfermedad,name='crearenfermedades'),
    path('enfermedades/',mostrarenfermedades,name='mostrarenfermedades'),
    path('editarenfermedades/<int:id>/',editarEnfermedadades,name='editarenfermedades'),
    path('eliminarenfermedades/<int:id>/',eliminarEnfermedadades,name='eliminarenfermedades'),

    path('crear_vacuna/', crearVacuna,name='crearvacuna'),
    path('vacuna/',mostrarvacuna,name='mostrarvacuna'),
    path('editarvacuna/<int:id>/',editarVacuna,name='editarvacuna'),
    path('eliminarvacuna/<int:id>/',eliminarVacuna,name='eliminarvacuna'),

    path('crear_cliente/', crearCliente,name='crearcliente'),
    path('cliente/',mostrarcliente,name='mostrarcliente'),
    path('editarcliente/<int:id>/',editarCliente,name='editarcliente'),
    path('eliminarcliente/<int:id>/',eliminarCliente,name='eliminarcliente'),

    path('crear_venta/', crearVenta,name='crearventa'),
    path('venta/',mostrarventa,name='mostrarventa'),
    path('editarventa/<int:id>/',editarVenta,name='editarventa'),
    path('eliminarventa/<int:id>/',eliminarVenta,name='eliminarventa'),

    path('crear_pajilla/', crearPajilla,name='crearpajilla'),
    path('pajilla/',mostrarpajilla,name='mostrarpajilla'),
    path('editarpajilla/<int:id>/',editarPajilla,name='editarpajilla'),
    path('eliminarpajilla/<int:id>/',eliminarPajilla,name='eliminarpajilla'),

    path('crear_vacamadre/', crearVacaMadre,name='crearvacamadre'),
    path('vacamadre/',mostrarvacamadre,name='mostrarvacamadre'),
    path('editarvacamadre/<int:id>/',editarVacaMadre,name='editarvacamadre'),
    path('eliminarvacamadre/<int:id>/',eliminarVacaMadre,name='eliminarvacamadre'),

    path('crear_evolucion/', crearEvolucion,name='crearevolucion'),
    path('evolucion/',mostrarevolucion,name='mostrarevolucion'),
    path('editarevolucion/<int:id>/',editarEvolucion,name='editarevolucion'),
    path('eliminarevolucion/<int:id>/',eliminarEvolucion,name='eliminarevolucion'),

    path('crear_ternero/', crearTernero,name='crearternero'),
    path('ternero/',mostrarternero,name='mostrarternero'),
    path('editarternero/<int:id>/',editarTernero,name='editarternero'),
    path('eliminarternero/<int:id>/',eliminarTernero,name='eliminarternero'),

    path('crear_baja/', crearBaja,name='crearbaja'),
    path('baja/',mostrarbaja,name='mostrarbaja'),
    path('editarbaja/<int:id>/',editarBaja,name='editarbaja'),
    path('eliminarbaja/<int:id>/',eliminarBaja,name='eliminarbaja'),

    path('crear_alimentacion/', crearAlimentacion,name='crearalimentacion'),
    path('alimentacion/',mostraralimentacion,name='mostraralimentacion'),
    path('editaralimentacion/<int:id>/',editarAlimentacion,name='editaralimentacion'),
    path('eliminaralimentacion/<int:id>/',eliminarAlimentacion,name='eliminaralimentacion')

]
