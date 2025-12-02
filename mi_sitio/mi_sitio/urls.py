"""
URL configuration for mi_sitio project.
"""
from django.contrib import admin
from django.urls import path, include  # ESTA DEBE SER TU IMPORTACIÓN

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mi_app.urls')), # ESTA DEBE SER LA LÍNEA DE CONEXIÓN
]