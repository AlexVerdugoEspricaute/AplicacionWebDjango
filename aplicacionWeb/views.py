
from django.shortcuts import render, redirect
from aplicacionWeb.models import Contacto
from aplicacionWeb.forms import ContactoForm
from . import forms
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomUserCreationForm


def index(request):
   return render(request,'index.html')

def calle(request):
    return render(request,'calle.html')

def galeria(request):
    return render(request, 'galeria.html')

def deportivas(request):
    return render(request, 'deportivas.html')

def terrenos(request):
    return render(request, 'terrenos.html')

def scooters(request):
    return render(request, 'scooters.html')

def contacto(request):
    form = forms.ContactoForm()
    if request.method == "POST":
        form = ContactoForm(request.POST)
    
        if form.is_valid():
            form.save()

        return redirect('index')
    
    data = {'form': form}
    return render(request, 'contacto.html', data)

def carrito(request):
    return render(request, 'carrito.html')


def registro(request):
    # Inicializar el formulario de registro de usuario
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        # Procesar el formulario de registro cuando se envía
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            # Guardar el nuevo usuario y autenticarlo
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            # Redirigir al usuario a la página de inicio después del registro exitoso
            return redirect(to="index")
        data["form"] = formulario
    # Renderizar la página de registro con el formulario correspondiente
    return render(request, 'registration/registro.html', data)

