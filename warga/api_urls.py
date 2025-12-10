from rest_framework.routers import DefaultRouter
from .views import WargaViewSet, PengaduanViewSet

app_name = 'api_modern'

router = DefaultRouter()
router.register(r'warga', WargaViewSet, basename='api-warga')
router.register(r'pengaduan', PengaduanViewSet, basename='api-pengaduan')

urlpatterns = router.urls
