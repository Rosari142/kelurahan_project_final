from django.urls import path
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Warga
from .serializers import WargaSerializer

class WargaListAPIView(ListAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer

class WargaDetailAPIView(RetrieveAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer


urlpatterns = [
    path('warga/', WargaListAPIView.as_view(), name='api-p6-warga-list'),
    path('warga/<int:pk>/', WargaDetailAPIView.as_view(), name='api-p6-warga-detail'),
]
