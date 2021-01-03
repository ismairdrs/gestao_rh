from django.contrib import admin
from .models import Documento


class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('descricao', )


admin.site.register(Documento, DocumentoAdmin)
