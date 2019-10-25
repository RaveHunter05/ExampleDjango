from rest_framework import routers
from .viewsets import *

router=routers.SimpleRouter()
router.register('productor', ProductorViewSet),
router.register('cantante', CantanteViewSet),
router.register('genero', GeneroViewSet),  
router.register('album', AlbumViewSet),   
router.register('tema', TemaViewSet),  
router.register('tema_productor', Tema_ProductorViewSet),
router.register('tema_cantante', Tema_CantanteViewSet),  
router.register('album_genero', Album_GeneroViewSet),
router.register('cliente', ClienteViewSet),
router.register('rol', RolViewSet),
router.register('usuario', UsuarioViewSet),
router.register('compra', CompraViewSet),
router.register('detalle_compra', Detalle_CompraViewSet),

urlpatterns = router.urls