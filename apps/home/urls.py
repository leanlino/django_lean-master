from django.urls import path
from .views import home, about, formulario
urlpatterns = [
    path('', home, name='home'),
    
    path('about/', about, name='about'),
    path('api/form', formulario, name='formulario')
]
