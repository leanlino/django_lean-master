
from django.urls import path
from .views import contact, submit

urlpatterns = [
    path('', contact, name='contact'),
    path('submit/', submit, name='submit'),
]
