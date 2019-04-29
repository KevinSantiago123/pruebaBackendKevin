from django.db import models

class Usuario(models.Model):

	#id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=255, null=False)
	apellido = models.CharField(max_length=255, null=False)
	direccion = models.CharField(max_length=255, null=False)
	ciudad = models.CharField(max_length=255, null=False)
	longitud = models.DecimalField(max_digits = 12, decimal_places = 6)
	latitud = models.DecimalField(max_digits = 12, decimal_places = 6)	        
	estadogeo = models.CharField(max_length=10, null=True)

	class Meta:
		ordering = ('nombre',)
    
	def __str__(self):
		return "{} ---- {} ---- {} ---- {} ---- {} ---- {} ---- {}".format(self.nombre, 
			self.apellido, 
			self.direccion,
			self.ciudad,
			self.longitud,
			self.latitud,
			self.estadogeo)

	