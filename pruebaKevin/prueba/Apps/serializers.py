from .models import Usuario
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Usuario
		fields = ('id','nombre','apellido','direccion','ciudad','longitud','latitud','estadogeo')

