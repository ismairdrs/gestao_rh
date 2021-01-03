from django.contrib import admin
from .models import RegistroHoraExtra


class RegistroHoraExtraAdmin(admin.ModelAdmin):
    list_display = ('motivo', )


admin.site.register(RegistroHoraExtra, RegistroHoraExtraAdmin)
