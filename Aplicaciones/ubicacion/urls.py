from django.urls import path
from . import views

urlpatterns = [ 
    path("sitios/", views.sitios_interes, name="Sitios"),
]