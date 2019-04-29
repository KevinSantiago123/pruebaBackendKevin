from rest_framework import viewsets, status
from .models import Usuario
from .serializers import UsuarioSerializer
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
import requests

class UsuarioView(viewsets.ModelViewSet):

	def recorrer(requests):
		queryset = Usuario.objects.all()
		for buscar in queryset:
			if buscar.longitud == 0:
				queryset_direccion = buscar.direccion
				queryset_ciudad = buscar.ciudad
				google_maps_url= 'https://maps.googleapis.com/maps/api/geocode/json?address='+queryset_direccion+','+queryset_ciudad+'&key=AIzaSyAYVHSbEo-Rh1qBeOOk_BKiXns7bzVniyQ'
				google_maps_json= requests.get(google_maps_url)
				result=google_maps_json.json()
				lgt = result.get('lng')
				lat = result.get('lat')
				buscar.longitud=lgt
				buscar.latitud=lat
		return queryset

	queryset = Usuario.objects.all()
	serializer_class = UsuarioSerializer
	
	


		






