from django.contrib import admin
from . import models
# Register your models here.
#untuk menampilkan data yang readonly
class ArtikelAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
        'updated',
        'published'
    ]

admin.site.register(models.Artikel, ArtikelAdmin)