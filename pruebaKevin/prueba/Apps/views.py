from rest_framework import viewsets, status
from .models import Usuario
from .serializers import UsuarioSerializer
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
import json

class UsuarioView(viewsets.ModelViewSet):

	def recorrer():
        queryset = Usuario.objects.all()
        for buscar in queryset:
            if buscar.longitud == 0:
                queryset_direccion = buscar.direccion
                queryset_ciudad = buscar.ciudad
            if __name__=='__main__':
                google_maps_url= 'https://maps.googleapis.com/maps/api/geocode/json?address='+queryset_direccion+','+queryset_ciudad+'&key=AIzaSyAYVHSbEo-Rh1qBeOOk_BKiXns7bzVniyQ'
                google_maps_json= requests.get(google_maps_url)
                if google_maps_json.status_code==200:
                    result=google_maps_json.json()
                    lgt = result ['results'][0]['geometry']['location']['lng']
                    lat = result ['results'][0]['geometry']['location']['lat']
                    buscar.longitud=lgt
                    buscar.latitud=lat
        return queryset

	queryset = Usuario.objects.all()
	serializer_class = UsuarioSerializer


		






