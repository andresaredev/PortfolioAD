from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout, authenticate
# Create your views here.

def inicio(request):
    return render(request,"pages/inicio.html",{})

def nosotros(request):
    return render(request,"pages/nosotros.html",{})

@login_required
def resumen(request):
    return render(request,"pages/resumen.html",{})

def Ingresar(request):
    if request.method == "GET": 
        return render(request,"registration/login.html",{})
    else: 
        usuario = request.POST["username"]
        contraseña = request.POST["contraseña"]

        user = authenticate(request, username=usuario, password=contraseña)
        login(request,user)

        return redirect('resumen')

def exit(request):
    logout(request)
    return redirect('Inicio')
