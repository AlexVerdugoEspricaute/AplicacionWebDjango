from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('calle/', views.calle, name='calle'),
    path('galeria/', views.galeria, name='galeria'),
    path('deportivas/', views.deportivas, name='deportivas'),
    path('terrenos/', views.terrenos, name='terrenos'),
    path('scooters', views.scooters, name='scooters'),
    path('contacto/', views.contacto, name='contacto'),
    path('carrito/', views.carrito, name='carrito'),
    path('registro/', views.registro, name='registro'), 
]
