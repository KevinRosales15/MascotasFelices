from rest_framework import serializers
from MascotasAPP.models import Citas, Desparasitacion, Propietario, Mascota, Historial

class PropietarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propietario
        fields = '__all__'

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'

class CitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citas
        fields = '__all__'

class DesparasitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desparasitacion
        fields = '__all__'

class HistorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historial
        fields = '__all__'