from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView

from MascotasAPP.models import Propietario, Mascota, Citas, Desparasitacion, Historial
from MascotasAPP.api.serializer import PropietarioSerializer, CitasSerializer, MascotaSerializer, DesparasitacionSerializer, HistorialSerializer

class PropietarioViewSet(viewsets.ModelViewSet):
    serializer_class = PropietarioSerializer
    queryset = Propietario.objects.all()


class MascotaViewSet(viewsets.ModelViewSet):
    serializer_class = MascotaSerializer
    queryset = Mascota.objects.all()

class CitasViewSet(viewsets.ModelViewSet):
    serializer_class = CitasSerializer
    queryset = Citas.objects.all()

class DesparacitacionesViewSet(viewsets.ModelViewSet):
    serializer_class = DesparasitacionSerializer
    queryset = Desparasitacion.objects.all()

class HistorialViewSet(viewsets.ModelViewSet):
    serializer_class = HistorialSerializer
    queryset = Historial.objects.all()
