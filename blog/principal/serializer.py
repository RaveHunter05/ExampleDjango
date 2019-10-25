from .models import *
from rest_framework import serializers

class ProductorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Productor
        fields='__all__'
        
class CantanteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cantante
        fields='__all__'

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genero
        fields='__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model=Album
        fields='__all__'

class TemaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tema
        fields='__all__'

class Tema_ProductorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tema_Productor
        fields='__all__'

class Tema_CantanteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tema_Cantante
        fields='__all__'

class Album_GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model=Album_Genero
        fields='__all__' 

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields='__all__'  

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rol
        fields='__all__'  

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields='__all__'                           

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model=Compra
        fields='__all__'

class Detalle_CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model=Detalle_Compra
        fields='__all__'        