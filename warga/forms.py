from django import forms
from .models import Warga, Pengaduan


class WargaForm(forms.ModelForm):
    class Meta:
        model = Warga
        fields = ['nik', 'nama_lengkap', 'alamat', 'no_telepon']  # pastikan field ini ada di model
        widgets = {
            'nik': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan NIK'}),
            'nama_lengkap': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama lengkap'}),
            'alamat': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Alamat lengkap'}),
            'no_telepon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nomor Telepon'}),
        }


class PengaduanForm(forms.ModelForm):
    class Meta:
        model = Pengaduan
        fields = ['pelapor', 'judul', 'deskripsi', 'status']  # ✅ ubah dari isi_laporan → deskripsi
        widgets = {
            'pelapor': forms.Select(attrs={'class': 'form-select'}),
            'judul': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Judul pengaduan'}),
            'deskripsi': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Isi laporan / deskripsi'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

