from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Contacto

def contacto(request):
    if request.method == "POST":
        tname = request.POST["name"]
        temail = request.POST["email"]
        tphone = request.POST["phone"]
        tmessage = request.POST["message"]
        obj_contact = Contacto(name=tname,email=temail,phone=tphone,message=tmessage)
        obj_contact.save()

        email(obj_contact)
        #return HttpResponse("El registro fue ingresado")
        return render(request,"pages/gracias.html",)
    return render(request,"pages/contacto.html",)

def email(contacto):
    subject = 'Thank you for contact me'
    message = f' Nombre: {contacto.name}\nEmail: {contacto.email}\nTeléfono: {contacto.phone}\nMensaje: {contacto.message}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['andresare0223@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return True