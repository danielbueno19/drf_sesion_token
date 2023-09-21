from django.db import models

class Persona(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    apellido = models.CharField('Apellido', max_length=200)

    #instanciamos la vsta por defecto, crea una vista para cada dato de la clase Persona
    def __str__(self):
        return '{0},{1}'.format(self.apellido, self.nombre)