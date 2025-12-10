from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Halaman Web
    path('', lambda request: redirect('warga_list')),  # Redirect ke list warga
    path('warga/', include('warga.urls')),  

    # API modern — Praktikum 7 & 9 (ViewSet + Router)
    path('api/', include('warga.api_urls')),

    # API Lama (Praktikum 6) tetap untuk dokumentasi
    path('api/v1/', include('warga.api_urls_p6')),

    # Token Auth — Praktikum 9
    path('api/auth/token/', obtain_auth_token, name='api-token-auth'),

    # Halaman login DRF (bawaan)
    path('api-auth/', include('rest_framework.urls')),
]
