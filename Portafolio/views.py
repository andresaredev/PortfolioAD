from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request,"pages/inicio.html",{})

def nosotros(request):
    return render(request,"pages/nosotros.html",{})

def resumen(request):
    return render(request,"pages/resumen.html",{})