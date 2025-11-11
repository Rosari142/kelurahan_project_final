from rest_framework import serializers
from .models import Warga, Pengaduan

class WargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warga
        fields = '__all__'


class PengaduanSerializer(serializers.ModelSerializer):
    pelapor = WargaSerializer(read_only=True)
    pelapor_id = serializers.PrimaryKeyRelatedField(
        queryset=Warga.objects.all(),
        source='pelapor',
        write_only=True
    )

    class Meta:
        model = Pengaduan
        fields = [
            'id',
            'judul',
            'deskripsi',
            'status',
            'tanggal_lapor',
            'pelapor',
            'pelapor_id'
        ]
        read_only_fields = ['tanggal_lapor']
