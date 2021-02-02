from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.

def contact(request):
    contact_form = ContactForm()# crear plantilla vacia

    if request.method == "POST":# se detecta si se envio por post
        contact_form = ContactForm(data=request.POST)# se llena con la información
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Envia el correo y redirecciona
            email = EmailMessage(
                "Alba Montoya: Nuevo mensaje de contacto",#asunto
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),#cuerpo del mensaje
                "no-contestar@inbox.mailtrap.io",#email origen
                ["roxanderve@gmail.com"],#email destino
                reply_to=[email]
            )

            try:
                email.send()
                #todo sale bien
                return redirect(reverse('contact')+"?ok")
            except:      
                #si sale mal se redireccioan a FAIL
                return redirect(reverse('contact')+"?fail")

    return render(request, "contact/contact.html", {"form":contact_form})