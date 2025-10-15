from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    # ketika buka root ("/"), langsung arahkan ke daftar warga
    path('', lambda request: redirect('warga_list')),
    path('warga/', include('warga.urls')),
]
