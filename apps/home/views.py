from django.shortcuts import render
from django.http import JsonResponse
from .models import Contacto
import json

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def formulario(request):
    contacto_front = request.body
    contacto_str = contacto_front.decode('utf-8') 
    contacto_diccionario = json.loads(contacto_str)
    #e print(type(contacto_diccionario))
    #print(contacto_diccionario['name'])
    
    contacto = Contacto(
        name = contacto_diccionario['name'],
        email = contacto_diccionario['email'],
        subject = contacto_diccionario['subject'],
        message = contacto_diccionario['message']
    )
    contacto.save()
    return JsonResponse({'success':'OK'}, status=200)
    