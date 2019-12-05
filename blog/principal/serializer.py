from .models import *
from rest_framework import serializers

class productorSerializer(serializers.ModelSerializer):
    class Meta:
        model=productor
        fields=('foto','portada','primer_nombre',
        'primer_apellido','nombre_artistico','bio')
        
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
        model=cancion_album
        fields='__all__'

class cancion_album_mixin_serializer(serializers.ModelSerializer):
    cancion=cancionSerializer()
    album=albumSerializer()
    class Meta:
        model=cancion_album
        fields=('cancion','album')

class cancion_generoSerializer(serializers.ModelSerializer):
    class Meta:
        model=cancion_genero
        fields='__all__'

class cancion_genero_mixin_serializer(serializers.ModelSerializer):
    cancion=cancionSerializer()
    genero=generoSerializer()
    class Meta:
        model=cancion_genero
        fields=('cancion','genero')

class album_generoSerializer(serializers.ModelSerializer):
    class Meta:
        model=album_genero
        fields='__all__'

class album_genero_mixin_serializer(serializers.ModelSerializer):
    album=albumSerializer()
    genero=generoSerializer()
    class Meta:
        model=album_genero
        fields=('album','genero')

class productor_cancionSerializer(serializers.ModelSerializer):
    class Meta:
        model=productor_cancion
        fields='__all__'

class productor_cancion_mixin_serializer(serializers.ModelSerializer):
    productor=productorSerializer()
    cancion=cancionSerializer()
    class Meta:
        model=productor_cancion
        fields=('productor','cancion')

class cantante_cancionSerializer(serializers.ModelSerializer):
    class Meta:
        model=cantante_cancion
        fields='__all__'

class cantante_cancion_mixin_serializer(serializers.ModelSerializer):
    cantante=cantanteSerializer()
    cancion=cancionSerializer()
    class Meta:
        model=cantante_cancion
        fields=('cantante','cancion')

class productor_albumSerializer(serializers.ModelSerializer):
    class Meta:
        model=productor_album
        fields='__all__'

class productor_album_mixin_serializer(serializers.ModelSerializer):
    productor=productorSerializer()
    album=albumSerializer()
    class Meta:
        model=productor_album
        fields=('productor','album')

class cantante_albumSerializer(serializers.ModelSerializer):
    class Meta:
        model=cantante_album
        fields='__all__'

class cantante_album_mixin_serializer(serializers.ModelSerializer):
    cantante=cantanteSerializer()
    album=albumSerializer()
    class Meta:
        model=cantante_album
        fields=('cantante','album')

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

class playlist_cancion_mixin_serializer(serializers.ModelSerializer):
    playlist=playlistSerializer()
    cancion_album=cancion_album_mixin_serializer()
    class Meta:
        model=playlist_cancion   
        fields=('playlist','cancion_album')  

        # componer esto  


class playlist_albumSerializer(serializers.ModelSerializer):
    class Meta:
        model=playlist_album
        fields='__all__'                 

class playlist_album_mixin_serializer(serializers.ModelSerializer):
    playlist=playlistSerializer()
    album=albumSerializer()
    class Meta:
        model=playlist_album
        fields=('playlist','album')   

class compraSerializer(serializers.ModelSerializer):
    class Meta:
        model=compra
        fields='__all__'

class compra_usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=compra_usuario
        fields='__all__'       

class compra_usuario_mixin_serializer(serializers.ModelSerializer):
    compra=compraSerializer()
    usuario=usuarioSerializer()
    class Meta:
        model=compra_usuario
        fields=('compra','usuario')       