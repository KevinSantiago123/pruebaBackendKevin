from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework import routers
from django.views.generic import TemplateView

router = routers.DefaultRouter() 
router.register('Usuario',views.UsuarioView)

urlpatterns = [
	path('',include(router.urls))
]

