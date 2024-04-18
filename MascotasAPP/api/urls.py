from rest_framework.routers import DefaultRouter
from MascotasAPP.api.views import DesparacitacionesViewSet, MascotaViewSet, CitasViewSet, PropietarioViewSet, HistorialViewSet

router = DefaultRouter()
router.register('Propietarios', PropietarioViewSet, basename='Propietario')
router.register(r'propietarios', PropietarioViewSet, basename='propietario')
router.register(r'mascotas', MascotaViewSet, basename='mascota')
router.register(r'citas', CitasViewSet, basename='citas')
router.register(r'desparacitaciones', DesparacitacionesViewSet, basename='desparacitaciones')
router.register(r'historial', HistorialViewSet, basename='historial')
urlpatterns = router.urls