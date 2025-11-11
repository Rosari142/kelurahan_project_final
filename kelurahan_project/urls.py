from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # HTML Web
    path('', lambda request: redirect('warga_list')),
    path('warga/', include('warga.urls')),

    # API Modern (ViewSet + Router)
    path('api/', include('warga.api_urls')),

    # API Praktikum 6 (ListAPIView + DetailAPIView)
    path('api/v1/', include('warga.api_urls_p6')),
]
