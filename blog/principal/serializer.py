from .models import *
from rest_framework import serializers

class productorSerializer(serializers.ModelSerializer):
    class Meta:
        model=productor
        fields='__all__'
        
class cantanteSerializer(serializers.ModelSerializer):
    class Meta:
        model=cantante
        fields='__all__'

class generoSerializer(serializers.ModelSerializer):
    class Meta:
        model=genero
        fields='__all__'

class albumSerializer(serializers.ModelSerializer):
    class Meta:
        model=album
        fields='__all__'

class cancionSerializer(serializers.ModelSerializer):
    class Meta:
        model=cancion
        fields='__all__'

class cancion_albumSerializer(serializers.ModelSerializer):
    class Meta:
        models=cancion_album
        fields='__all__'

class cancion_generoSerializer(serializers.ModelSerializer):
    class Meta:
        model=cancion_genero
        fields='__all__'

class album_generoSerializer(serializers.ModelSerializer):
    class Meta:
        model=album_genero
        fields='__all__'

class productor_cancionSerializer(serializers.ModelSerializer):
    class Meta:
        model=productor_cancion
        fields='__all__'

class cantante_cancionSerializer(serializers.ModelSerializer):
    class Meta:
        model=cantante_cancion
        fields='__all__'

class productor_albumSerializer(serializers.ModelSerializer):
    class Meta:
        model=productor_album
        fields='__all__'

class cantante_albumSerializer(serializers.ModelSerializer):
    class Meta:
        model=cantante_album
        fields='__all__'

class suscriptorSerializer(serializers.ModelSerializer):
    class Meta:
        model=suscriptor
        fields='__all__'  

class tarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model=tarjeta
        fields='__all__'

class membresiaSerializer(serializers.ModelSerializer):
    class Meta:
        model=membresia
        fields='__all__'

class rolSerializer(serializers.ModelSerializer):
    class Meta:
        model=rol
        fields='__all__'  

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=usuario
        fields='__all__'

class playlistSerializer(serializers.ModelSerializer):
    class Meta:
        model=playlist
        fields='__all__'   

class playlist_cancionSerializer(serializers.ModelSerializer):
    class Meta:
        model=playlist_cancion   
        fields='__all__'    

class playlist_albumSerializer(serializers.ModelSerializer):
    class Meta:
        model=playlist_album
        fields='__all__'                 

class compraSerializer(serializers.ModelSerializer):
    class Meta:
        model=compra
        fields='__all__'

class compra_usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=compra_usuario
        fields='__all__'        