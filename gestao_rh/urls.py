from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('funcionarios/', include('apps.funcionarios.urls')),
    #path('departamentos/', include('apps.departamentos.urls')),
    path('empresas/', include('apps.empresas.urls')),
    #path('registro_hora_extra/', include('apps.registro_hora_extra.urls')),
    path('', include('apps.core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]
