from django.contrib import admin
from .models import Artikel, Kategori

@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    list_display = ('nama', 'created_at', 'created_by')
    search_fields = ('nama',)
    list_filter = ('created_at',)

@admin.register(Artikel)
class ArtikelAdmin(admin.ModelAdmin):
    list_display = ('judul', 'kategori', 'created_at', 'created_by', 'status')
    search_fields = ('judul', 'isi')
    list_filter = ('status', 'created_at', 'kategori')
