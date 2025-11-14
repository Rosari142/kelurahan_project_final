from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Halaman web
    path('', lambda request: redirect('warga_list')),  # Redirect root ke daftar warga
    path('warga/', include('warga.urls')),           # URL untuk web page

    # API Modern (ViewSet + Router) - praktikum 7
    path('api/', include('warga.api_urls')),

    # API Lama (ListAPIView + DetailAPIView) - praktikum 6, tetap disimpan
    path('api/v1/', include('warga.api_urls_p6')),
]
