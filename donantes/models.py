from django.db import models

# Create your models here.

class Donador(models.Model):
	categoria = models.CharField(max_length=20, default='')
	nombre = models.CharField(max_length=100)
	telefono = models.CharField(max_length=14)
	email = models.EmailField(max_length=200)
	sexo = models.CharField(max_length=20)
	tipo = models.CharField(max_length=3)
	centro = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre