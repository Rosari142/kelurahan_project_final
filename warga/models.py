from django.db import models

class Warga(models.Model):
    nik = models.CharField(max_length=20, blank=True)
    nama_lengkap = models.CharField(max_length=200)
    alamat = models.CharField(max_length=255, blank=True)
    no_telepon = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nama_lengkap


class Pengaduan(models.Model):
    STATUS_CHOICES = [
        ('BARU', 'Baru'),
        ('DIPROSES', 'Diproses'),
        ('SELESAI', 'Selesai'),
    ]
    judul = models.CharField(max_length=200)
    deskripsi = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='BARU')
    tanggal_lapor = models.DateTimeField(auto_now_add=True)
    pelapor = models.ForeignKey('warga.Warga', on_delete=models.CASCADE, related_name='pengaduan')

    def __str__(self):
        return self.judul

