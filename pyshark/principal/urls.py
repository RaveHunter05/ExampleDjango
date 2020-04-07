from rest_framework import routers
from .viewsets import *

router=routers.SimpleRouter()
router.register('productor', productorViewSet),
router.register('cantante', cantanteViewSet),
router.register('genero', generoViewSet),  
router.register('album', albumViewSet),   
router.register('cancion', cancionViewSet),
router.register('cancion_album', cancion_albumViewSet),
router.register('cancion_genero', cancion_generoViewSet),
router.register('album_genero', album_generoViewSet),
router.register('productor_cancion', productor_cancionViewSet),
router.register('cantante_cancion', cantante_cancionViewSet),
router.register('productor_album', productor_albumViewSet),
router.register('cantante_album', cantante_albumViewSet),  
router.register('suscriptor', suscriptorViewSet),
router.register('tarjeta', tarjetaViewSet),
router.register('membresia', membresiaViewSet),
router.register('rol', rolViewSet),
router.register('usuario', usuarioViewSet),
router.register('playlist', playlistViewSet),
router.register('playlist_cancion', playlist_cancionViewSet),
router.register('playlist_album', playlist_albumViewSet),
router.register('compra', compraViewSet),
router.register('compra_usuario', compra_usuarioViewSet),
router.register('cancion_album_mixin', cancion_album_mixin_viewset)
router.register('cancion_genero_mixin', cancion_genero_mixin_viewset)
router.register('album_genero_mixin', album_genero_mixin_viewset)
router.register('productor_cancion_mixin', productor_cancion_mixin_viewset)
router.register('cantante_cancion_mixin', cantante_cancion_mixin_viewset)
router.register('productor_album_mixin', productor_album_mixin_viewset)
router.register('cantante_album_mixin', cantante_album_mixin_viewset)
router.register('playlist_cancion_mixin', playlist_cancion_mixin_viewset)
router.register('compra_usuario_mixin', compra_usuario_mixin_viewset),
router.register('playlist_album_mixin', playlist_album_mixin_viewset),








urlpatterns = router.urls