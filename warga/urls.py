from django.urls import path
from .views import (
    WargaListView,
    WargaDetailView,
    PengaduanListView,
    WargaCreateView,
    PengaduanCreateView,
)

urlpatterns = [
    path('', WargaListView.as_view(), name='warga_list'),        # GET → list semua warga
    path('tambah/', WargaCreateView.as_view(), name='warga_create'),  # POST → tambah warga
    path('<int:pk>/', WargaDetailView.as_view(), name='warga_detail'), # GET, PUT, DELETE → detail warga
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan_list'),
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan_create'),
]
