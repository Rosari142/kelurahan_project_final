from django.urls import path
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Warga
from .serializers import WargaSerializer

app_name = 'api_p6'

class WargaListAPIView(ListAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer
    permission_classes = [IsAuthenticated]  # wajib pakai token

class WargaDetailAPIView(RetrieveAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer
    permission_classes = [IsAuthenticated]  # wajib pakai token

urlpatterns = [
    path('warga/', WargaListAPIView.as_view(), name='api-p6-warga-list'),
    path('warga/<int:pk>/', WargaDetailAPIView.as_view(), name='api-p6-warga-detail'),
]
