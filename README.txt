
Aplikasi Kelurahan - Project Final
=================================

Fitur:
- Tambah Warga Baru
- Tambah Pengaduan Baru (dengan dropdown Warga)

Persyaratan:
- Python 3.10+ recommended
- Django 5.x

Cara Menjalankan:
1. (Opsional) Buat virtual environment:
   python -m venv venv
   source venv/bin/activate    # Linux / macOS
   venv\Scripts\activate     # Windows

2. Install dependencies (jika diperlukan):
   pip install django

3. Buat migrasi dan terapkan:
   python manage.py makemigrations
   python manage.py migrate

4. Jalankan server:
   python manage.py runserver

5. Buka browser:
   http://127.0.0.1:8000/warga/
   http://127.0.0.1:8000/warga/tambah/
   http://127.0.0.1:8000/pengaduan/tambah/

Catatan:
- Jika project menggunakan nama app selain 'warga', sesuaikan URL dan INSTALLED_APPS di settings.py.
- Jika Anda ingin melihat daftar pengaduan, pastikan ada PengaduanListView atau buat view sederhana.
