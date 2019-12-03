from rest_framework import viewsets
from .models import *
from .serializer import *

class productorViewSet(viewsets.ModelViewSet):
    queryset=productor.objects.all()
    serializer_class=productorSerializer

class cantanteViewSet(viewsets.ModelViewSet):
    queryset=cantante.objects.all()
    serializer_class=cantanteSerializer

class generoViewSet(viewsets.ModelViewSet):
    queryset=genero.objects.all()
    serializer_class=generoSerializer

class albumViewSet(viewsets.ModelViewSet):
    queryset=album.objects.all()
    serializer_class=albumSerializer  

class cancionViewSet(viewsets.ModelViewSet):
    queryset=cancion.objects.all()
    serializer_class=cancionSerializer 

class cancion_albumViewSet(viewsets.ModelViewSet):
    queryset=cancion_album.objects.all()
    serializer_class=cancion_albumSerializer

class cancion_generoViewSet(viewsets.ModelViewSet):
    queryset=cancion_genero.objects.all()
    serializer_class=cancion_generoSerializer

class album_generoViewSet(viewsets.ModelViewSet):
    queryset=album_genero.objects.all()
    serializer_class=album_generoSerializer

class productor_cancionViewSet(viewsets.ModelViewSet):
    queryset=productor_cancion.objects.all()
    serializer_class=productor_cancionSerializer

class cantante_cancionViewSet(viewsets.ModelViewSet):
    queryset=cantante_cancion.objects.all()
    serializer_class=cantante_cancionSerializer

class productor_albumViewSet(viewsets.ModelViewSet):
    queryset=productor_album.objects.all()
    serializer_class=productor_albumSerializer

class cantante_albumViewSet(viewsets.ModelViewSet):
    queryset=cantante_album.objects.all()
    serializer_class=cantante_albumSerializer

class suscriptorViewSet(viewsets.ModelViewSet):
    queryset=suscriptor.objects.all()
    serializer_class=suscriptorSerializer

class tarjetaViewSet(viewsets.ModelViewSet):
    queryset=tarjeta.objects.all()
    serializer_class=tarjetaSerializer

class membresiaViewSet(viewsets.ModelViewSet):
    queryset=membresia.objects.all()
    serializer_class=membresiaSerializer

class rolViewSet(viewsets.ModelViewSet):
    queryset=rol.objects.all()
    serializer_class=rolSerializer  

class usuarioViewSet(viewsets.ModelViewSet):
    queryset=usuario.objects.all()
    serializer_class=usuarioSerializer  

class playlistViewSet(viewsets.ModelViewSet):
    queryset=playlist.objects.all()
    serializer_class=playlistSerializer

class playlist_cancionViewSet(viewsets.ModelViewSet):
    queryset=playlist_cancion.objects.all()
    serializer_class=playlist_cancionSerializer

class playlist_albumViewSet(viewsets.ModelViewSet):
    queryset=playlist_album.objects.all()
    serializer_class=playlist_albumSerializer

class compraViewSet(viewsets.ModelViewSet):
    queryset=compra.objects.all()
    serializer_class=compraSerializer  

class compra_usuarioViewSet(viewsets.ModelViewSet):
    queryset=compra_usuario.objects.all()
    serializer_class=compra_usuarioSerializer



