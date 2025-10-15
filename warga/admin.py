from django.contrib import admin
from .models import Warga, Pengaduan

@admin.register(Warga)
class WargaAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'nik', 'alamat')
    search_fields = ('nama_lengkap', 'nik')

@admin.register(Pengaduan)
class PengaduanAdmin(admin.ModelAdmin):
    list_display = ('judul', 'pelapor', 'status', 'tanggal_lapor')
    list_filter = ('status',)
    search_fields = ('judul', 'pelapor__nama_lengkap')
