from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),

    # HTML
    path('', lambda request: redirect('warga_list')),
    path('warga/', include('warga.urls')),

    # API (baru)
    path('api/', include('warga.api_urls')),
]
