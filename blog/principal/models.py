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

#---------------------------------------- Artistas, Canciones, Álbumes, ---------------------------------
    
class productor(models.Model):
    foto=models.ImageField(upload_to='pic_folder/', blank=True)
    portada=models.ImageField(upload_to='pic_folder/' , blank=True)
    primer_nombre=models.CharField(max_length=50)
    primer_apellido=models.CharField(max_length=50)
    nombre_artistico=models.CharField(max_length=50)
    bio=models.TextField(blank=True)

    def __str__(self):
        return self.nombre_artistico

class cantante(models.Model):
    foto=models.ImageField(upload_to='pic_folder/' , blank=True)
    portada=models.ImageField(upload_to='pic_folder/' , blank=True)
    primer_nombre=models.CharField(max_length=50)
    primer_apellido=models.CharField(max_length=50)
    nombre_artistico=models.CharField(max_length=50)
    bio=models.TextField(blank=True)

    def __str__(self):
        return self.nombre_artistico

class genero(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class album(models.Model):
    caratula=models.ImageField(upload_to='pic_folder/')
    titulo=models.CharField(max_length=50)
    corazon=models.BooleanField(default=False)
    tipo=models.CharField(max_length=40)
    fecha_lanzamiento=models.DateField(auto_now_add=True)
    duracion=models.TimeField()
    descripcion=models.TextField(blank=True)

    def __str__(self):
        return self.titulo

class cancion(models.Model):
    caratula=models.ImageField(upload_to='pic_folder/' , blank=True)
    titulo=models.CharField(max_length=50)
    corazon=models.BooleanField(default=False)
    duracion=models.TimeField()
    fecha_lanzamiento=models.DateField(auto_now_add=True)
    sonido=models.FileField(upload_to='musica/', blank=True)

    def __str__(self):
        return self.titulo

class cancion_album(models.Model):
    cancion=models.ForeignKey(cancion, blank=True, null=True, on_delete=models.SET_NULL)
    album=models.ForeignKey(album, blank=True, null=True, on_delete=models.SET_NULL)

class cancion_genero(models.Model):
    cancion=models.ForeignKey(cancion, blank=True, null=True, on_delete=models.SET_NULL)
    genero=models.ForeignKey(genero, blank=True, null=True, on_delete=models.SET_NULL)

class album_genero(models.Model):
    album=models.ForeignKey(album, blank=True, null=True, on_delete=models.SET_NULL)
    genero=models.ForeignKey(genero, blank=True, null=True, on_delete=models.SET_NULL)

class productor_cancion(models.Model):
    productor=models.ForeignKey(productor, blank=True, null=True, on_delete=models.SET_NULL)
    cancion=models.ForeignKey(cancion, blank=True, null=True, on_delete=models.SET_NULL)

class cantante_cancion(models.Model):
    cantante=models.ForeignKey(cantante, blank=True, null=True, on_delete=models.SET_NULL)
    cancion=models.ForeignKey(cancion, blank=True, null=True, on_delete=models.SET_NULL)

class productor_album(models.Model):
    productor=models.ForeignKey(productor, blank=True, null=True, on_delete=models.SET_NULL)
    album=models.ForeignKey(album, blank=True, null=True, on_delete=models.SET_NULL)

class cantante_album(models.Model):
    cantante=models.ForeignKey(cantante, blank=True, null=True, on_delete=models.SET_NULL)
    album=models.ForeignKey(album, blank=True, null=True, on_delete=models.SET_NULL)

#------------------------------------------ Login, Autenticación, Suscriptor, Tarjeta, Playlist -------------------------------------

class suscriptor(models.Model):
    primer_nombre=models.CharField(max_length=50)
    primer_apellido=models.CharField(max_length=50)
    pais_ubicacion=models.CharField(max_length=50)
    fecha_nacimiento=models.DateField()
    telefono=models.CharField(max_length=30)

    def __str__(self):
        return self.primer_nombre

class tarjeta(models.Model):
    suscriptor=models.ForeignKey(suscriptor, blank=True, null=True, on_delete=models.SET_NULL)
    numero_tarjeta=models.CharField(max_length=150, unique=True) #Ver posibilidad de aplicar hash, salt or pepper
    tipo=models.CharField(max_length=30)
    fecha_emision=models.DateField()
    fecha_vencimiento=models.DateField()

    def __str__(self):
        return self.numero_tarjeta

class membresia(models.Model):
    titulo=models.CharField(max_length=30)
    descripcion=models.TextField(blank=True)
    precio=models.DecimalField(max_digits=4, decimal_places=2)
    estado=models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class rol(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class usuario(models.Model):
    rol=models.ForeignKey(rol, blank=True, null=True, on_delete=models.SET_NULL)
    suscriptor=models.ForeignKey(suscriptor, blank=True, null=True, on_delete=models.SET_NULL)
    foto=models.ImageField(upload_to='pic_folder/' , blank=True)
    portada=models.ImageField(upload_to='pic_folder/', blank=True)
    nombre_usuario=models.CharField(max_length=50, unique=True)
    nickname=models.CharField(max_length=50) #agregado nickname, Baldor
    contraseña=models.CharField(max_length=150) #Ver posibilidad de aplicar hash, salt or pepper
    correo=models.EmailField(unique=True)
    premium=models.BooleanField(default=False)

    def __str__(self):
        return self.nombre_usuario

class playlist(models.Model):
    # --> Usuarios no pueden agregar carátulas a las playlists  <-- Importante
    usuario=models.ForeignKey(usuario, blank=True, null=True, on_delete=models.SET_NULL)
    titulo=models.CharField(max_length=50)
    corazon=models.BooleanField(default=False)
    fecha_creacion=models.DateField(auto_now_add=True)
    fecha_modificacion=models.DateField(auto_now=True) # --> Verificar uso de auto_now ó auto_now_add para modificaciones en registros
    duracion=models.TimeField()
    descripcion=models.TextField(blank=True)

    def __str__(self):
        return self.titulo

class playlist_cancion(models.Model):
    playlist=models.ForeignKey(playlist, blank=True, null=True, on_delete=models.SET_NULL)
    cancion_album=models.ForeignKey(cancion_album, blank=True, null=True, on_delete=models.SET_NULL)

class playlist_album(models.Model):
    playlist=models.ForeignKey(playlist, blank=True, null=True, on_delete=models.SET_NULL)
    album=models.ForeignKey(album, blank=True, null=True, on_delete=models.SET_NULL)

#------------------------------------ Adquisición de suscripción premium ---------------------------------------------------

class compra(models.Model):
    membresia=models.ForeignKey(membresia, blank=True, null=True, on_delete=models.SET_NULL)
    usuario=models.ForeignKey(usuario, blank=True, null=True, on_delete=models.SET_NULL)
    concepto=models.TextField(blank=True)
    monto=models.DecimalField(max_digits=4, decimal_places=2)
    fecha_compra=models.DateField(auto_now_add=True)
    descuento=models.DecimalField(max_digits=2, decimal_places=2)
    # monto deberia ser un campo calculado, por tanto nulo

class compra_usuario(models.Model):
    compra=models.ForeignKey(compra, blank=True, null=True, on_delete=models.SET_NULL)
    usuario=models.ForeignKey(usuario, blank=True, null=True, on_delete=models.SET_NULL)
    fecha_expiracion=models.DateField()
    # fecha de expiracion es otro campo calculado, por tanto deberia ser nulo








