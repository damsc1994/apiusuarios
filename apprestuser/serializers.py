from rest_framework import serializers
from .models import Usuarios, Personas


class UsuarioSerialize(serializers.ModelSerializer):
    class Meta:
       model = Usuarios
       fields = ('id', 'nombre_usuario', 'correo', 'contrasena','persona')
        
class PersonasSerialize(serializers.ModelSerializer):
    personas = UsuarioSerialize(many=True,read_only=True)
    class Meta:
        model = Personas
        fields = ('id', 'nombres', 'apellidos', 'edad', 'direccion', 'personas')








