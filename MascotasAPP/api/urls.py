from rest_framework.routers import DefaultRouter
from MascotasAPP.api.views import DesparacitacionesViewSet, MascotaViewSet, CitasViewSet, PropietarioViewSet, HistorialViewSet

router = DefaultRouter()
router.register('Propietarios', PropietarioViewSet, basename='Propietario')
router.register('mascotas', MascotaViewSet, basename='mascota')
router.register('citas', CitasViewSet, basename='citas')
router.register('desparacitaciones', DesparacitacionesViewSet, basename='desparacitaciones')
router.register('historial', HistorialViewSet, basename='historial')
urlpatterns = router.urls