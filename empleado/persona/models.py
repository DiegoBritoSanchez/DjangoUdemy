from django.db import models

from empleado.applications.departamento.models import Departamento

# Create your models here.
class Empleado(models.Model):

    jobs = (
        ('0', 'contable')
        ('1', 'administrador')
        ('2', 'economista')
    )

    firstName = models.CharField('Nombre', max_length=60)
    lastName = models.CharField('Apellidos', max_length=60)
    job = models.CharField('Trabajo', max_length=1, choices=jobs)
    departament = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    #image = models.ImageField('Imagen', upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return str(self.id) + ' ' + self.firstName + ' ' + self.lastName