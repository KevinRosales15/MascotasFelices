from django.db import models

class Propietario(models.Model):
    propie_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()

    class Meta:
        verbose_name = ""
        verbose_name_plural = "s"
        constraints = [
            models.UniqueConstraint(fields=['nombre', 'correo'], name='unique_cita')
        ]
        
    def __str__(self) -> str:
        return f'{self.propie_id}-{self.nombre}'

class Mascota(models.Model):
    mascota_id = models.AutoField(primary_key=True)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    Raza = models.CharField(max_length=50)
    Especie = models.CharField(max_length=50)
    Fecha_nacimiento = models.DateField()
    Edad = models.IntegerField()
    Sexo = models.CharField(max_length=10,choices=[('M', 'Macho'), ('H', 'Hembra')], default='M')
    Color = models.CharField(max_length=250)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()

    def __str__(self) -> str:
        return self.nombre

class Citas(models.Model):
    cita_id = models.AutoField(primary_key=True)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha_y_hora = models.DateTimeField()
    descripcion = models.CharField(max_length=255)
    lugar = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f'{self.mascota} - {self.fecha_y_hora}'
    
class Desparasitacion(models.Model):
    cartilla_id = models.AutoField(primary_key=True)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha = models.DateField()
    tratamiento = models.CharField(max_length=100)
    tipo_medicamento = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f'{self.mascota} - {self.fecha}'
    
class Historial(models.Model):
    store_id = models.AutoField(primary_key=True)
    historial = models.CharField(max_length=500)

    def __str__ (self)-> str:
        return f'{self.historial}'