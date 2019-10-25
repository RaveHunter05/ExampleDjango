from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    author=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField()
    created_table=models.DateTimeField(
        default=timezone.now)
    published_date=models.DateTimeField(
        blank=True, null=True)
    
    def publish(self):
        self.published_date=timezone.now
        self.save
    
    def __str__(self):
        return self.title

#---------------------------------------- Personas, Temas, Album ---------------------------------
    
class Productor(models.Model):
    Nombre=models.CharField(max_length=50)
    Apellido=models.CharField(max_length=50)
    Nombre_artistico=models.CharField(max_length=50)

class Cantante(models.Model):
    Nombre=models.CharField(max_length=50)
    Apellido=models.CharField(max_length=50)
    Nombre_artistico=models.CharField(max_length=50)

class Genero(models.Model):
    Nombre=models.CharField(max_length=30)
    Descripcion=models.TextField(blank=True)

class Album(models.Model):
    Nombre=models.CharField(max_length=60)
    Tipo_album=models.CharField(max_length=30)
    Fecha_lanzamiento=models.DateField(auto_now=True)
    Duracion_album=models.TimeField()
    '''Duracion=models.                     Investigar tipo de campo para manejar 
                                                        los tiempos hh//mm//ss
    '''
    Estrellas=models.IntegerField() #Validar valor maximo entre 1-5
    Imagen=models.ImageField(upload_to='pic_folder/')


class Tema(models.Model):
    Genero=models.ForeignKey(Genero, on_delete=models.CASCADE)
    Album=models.ForeignKey(Album, on_delete=models.CASCADE)
    Titulo=models.CharField(max_length=60)
    '''Duracion=models.                     Investigar tipo de campo para manejar 
                                                        los tiempos hh//mm//ss
    '''
    Estrellas=models.IntegerField() #Validar valor maximo entre 1-5
    Fecha_lanzamiento=models.DateField(auto_now=True)
    Precio=models.DecimalField(max_digits=10, decimal_places=2)
    Duracion_album=models.TimeField()
    Imagen=models.ImageField(upload_to='pic_folder/')


class Tema_Productor(models.Model):
    Productor=models.ForeignKey(Productor, on_delete=models.CASCADE)
    Tema=models.ForeignKey(Tema, on_delete=models.CASCADE)

class Tema_Cantante(models.Model):
    Cantante=models.ForeignKey(Cantante, on_delete=models.CASCADE)
    Tema=models.ForeignKey(Tema, on_delete=models.CASCADE)

class Album_Genero(models.Model):
    Album=models.ForeignKey(Album, on_delete=models.CASCADE)
    Genero=models.ForeignKey(Genero, on_delete=models.CASCADE)

#------------------------------------------ Login y Autenticación -------------------------------------

class Cliente(models.Model):
    Nombre=models.CharField(max_length=50)
    Apellido=models.CharField(max_length=50)

class Rol(models.Model):
    Descripcion=models.CharField

class Usuario(models.Model):
    Rol=models.ForeignKey(Rol,on_delete=models.CASCADE)
    Cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Nombre_Usuario=models.CharField(max_length=50)
    Contraseña=models.CharField(max_length=128)
    Correo=models.EmailField(unique=True)
    Estado=models.BooleanField(default=True)


#------------------------------------ Venta de temas ---------------------------------------------------

class Compra(models.Model):
    Cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Fecha_realizacion=models.DateField(auto_now=True)
    Concepto=models.TextField(blank=True)
    Monto=models.DecimalField(max_digits=10,decimal_places=2)

class Detalle_Compra(models.Model):
    Compra=models.ForeignKey(Compra, on_delete=models.CASCADE)
    Tema=models.ForeignKey(Tema, on_delete=models.CASCADE)
    Album=models.ForeignKey(Album, on_delete=models.CASCADE)
    Fecha_realizacion=models.DateField(auto_now=True)
    Cantidad=models.PositiveIntegerField()
    Precio=models.DecimalField(max_digits=10,decimal_places=2)







