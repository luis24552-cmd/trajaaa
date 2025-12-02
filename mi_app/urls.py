# mi_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('actividades/', views.actividades, name='actividades'),
    path('diagnostico/', views.diagnostico, name='diagnostico'),
    path('galeria/', views.galeria, name='galeria'),
]
