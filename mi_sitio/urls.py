# mi_sitio/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # CAMBIA 'home/' a la ruta vacía (root)
    path('', include('mi_app.urls')), # <--- ¡ESTA ES LA LÍNEA CORRECTA!
]