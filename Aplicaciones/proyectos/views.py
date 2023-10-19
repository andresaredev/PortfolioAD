from django.shortcuts import render
from .models import Proyecto

def proyectos(request):
    mis_proyectos = Proyecto.objects.all()
    return render(request,"proyectos.html",{"proyectos":mis_proyectos})
# Create your views here.
