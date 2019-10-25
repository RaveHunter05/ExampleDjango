from rest_framework import viewsets
from .models import *
from .serializer import *

class ProductorViewSet(viewsets.ModelViewSet):
    queryset=Productor.objects.all()
    serializer_class=ProductorSerializer


class CantanteViewSet(viewsets.ModelViewSet):
    queryset=Cantante.objects.all()
    serializer_class=CantanteSerializer

class GeneroViewSet(viewsets.ModelViewSet):
    queryset=Genero.objects.all()
    serializer_class=GeneroSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset=Album.objects.all()
    serializer_class=AlbumSerializer    

class TemaViewSet(viewsets.ModelViewSet):
    queryset=Tema.objects.all()
    serializer_class=TemaSerializer

class Tema_ProductorViewSet(viewsets.ModelViewSet):
    queryset=Tema_Productor.objects.all()
    serializer_class=Tema_ProductorSerializer    

class Tema_CantanteViewSet(viewsets.ModelViewSet):
    queryset=Tema_Cantante.objects.all()
    serializer_class=Tema_CantanteSerializer 

class Album_GeneroViewSet(viewsets.ModelViewSet):
    queryset=Album_Genero.objects.all()
    serializer_class=Album_GeneroSerializer  

class ClienteViewSet(viewsets.ModelViewSet):
    queryset=Cliente.objects.all()
    serializer_class=ClienteSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset=Rol.objects.all()
    serializer_class=RolSerializer  

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset=Usuario.objects.all()
    serializer_class=UsuarioSerializer  

class CompraViewSet(viewsets.ModelViewSet):
    queryset=Compra.objects.all()
    serializer_class=CompraSerializer  

class Detalle_CompraViewSet(viewsets.ModelViewSet):
    queryset=Detalle_Compra.objects.all()
    serializer_class=Detalle_CompraSerializer



