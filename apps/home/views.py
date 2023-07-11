from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Contacto
import json
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def formulario(request):
    if request.method == 'POST':
        contacto_front = request.body
        contacto_str = contacto_front.decode('utf-8') 
        contacto_diccionario = json.loads(contacto_str)
        print(type(contacto_diccionario))
        print(contacto_diccionario)
        
        contacto = Contacto(
            name = contacto_diccionario['name'],
            email = contacto_diccionario['email'],
            subject = contacto_diccionario['subject'],
            message = contacto_diccionario['message']
        )
        contacto.save()
        return redirect('home')

    # Agrega un HttpResponse para cuando no es una petición POST
    else:
        return HttpResponse('Método no permitido', status=405)
        
    