from django.contrib import admin
from .models import Empresa


class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome',)


admin.site.register(Empresa, EmpresaAdmin)
