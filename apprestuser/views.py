from django.shortcuts import render
from .models import Usuarios, Personas
from .serializers import UsuarioSerialize, PersonasSerialize
from rest_framework import viewsets

# Create your views here.


class UsuarioViewset(viewsets.ModelViewSet):
    serializer_class = UsuarioSerialize
    queryset = Usuarios.objects.all()

class PersonaViewset(viewsets.ModelViewSet):
    serializer_class = PersonasSerialize
    queryset = Personas.objects.all()