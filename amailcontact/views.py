from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def contactForm(request):
    return render(request, 'contact-form.html')

def contact(request):
    if request.method == 'POST':
        asunto = request.POST['txtAsunto']
        mensaje = request.POST['txtMensaje'] + " / Email: " + request.POST['txtEmail']        
        email_desde = settings.EMAIL_HOST_USER
        email_para = ['esgaelramos@gmail.com']
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=True)
        return render(request, 'contact-success.html')
    return render(request, 'contact-form.html')
