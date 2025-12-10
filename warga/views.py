from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm

# ==========================
# VIEW HTML (TIDAK DIUBAH)
# ==========================

class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html'
    context_object_name = 'warga_list'


class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'
    context_object_name = 'object'


class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'
    context_object_name = 'object_list'


class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga_list')


class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan_list')



# ==========================
# API VIEWSET (P6 PRAKTIKUM 5)
# ==========================

from rest_framework import viewsets, filters
from .serializers import WargaSerializer, PengaduanSerializer

class WargaViewSet(viewsets.ModelViewSet):
    queryset = Warga.objects.all().order_by('nama_lengkap')
    serializer_class = WargaSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nik', 'nama_lengkap', 'alamat', 'no_telepon']
    ordering_fields = ['nama_lengkap', 'nik']


class PengaduanViewSet(viewsets.ModelViewSet):
    queryset = Pengaduan.objects.all().order_by('-tanggal_lapor')
    serializer_class = PengaduanSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['judul', 'deskripsi', 'status', 'pelapor__nama_lengkap']
    ordering_fields = ['tanggal_lapor', 'status']



# ==========================
# API P6 – ListAPIView & DetailAPIView
# ==========================

from rest_framework.generics import ListAPIView, RetrieveAPIView

class WargaListAPIView(ListAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer


class WargaDetailAPIView(RetrieveAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer
