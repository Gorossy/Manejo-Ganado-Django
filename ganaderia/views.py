from django.forms.forms import Form
from django.shortcuts import redirect, render
from .forms import UserRegisterForm

# Create your views here.
def inicio(request):
    return render(request,'index.html')


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
