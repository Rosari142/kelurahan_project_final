# kelurahan_project (Django)

Project demo untuk praktikum Framework Programming — Pertemuan 2.

Fitur:
- Model `Warga` dan `Pengaduan` (One-to-Many)
- Halaman daftar warga, detail warga (dengan daftar pengaduan), dan daftar semua pengaduan
- Contoh data sudah disediakan di `fixtures/initial_data.json`

## Cara menjalankan (ringkas)

1. Buat virtual environment & aktifkan (direkomendasikan)
   ```bash
   python -m venv env
   source env/bin/activate   # Linux/macOS
   env\Scripts\activate    # Windows
   ```

2. Install dependency
   ```bash
   pip install -r requirements.txt
   ```

3. Jalankan migrasi
   ```bash
   python manage.py migrate
   ```

4. Muat data contoh
   ```bash
   python manage.py loaddata fixtures/initial_data.json
   ```

5. Jalankan server
   ```bash
   python manage.py runserver
   ```

6. Buka di browser:
   - Daftar warga: http://127.0.0.1:8000/warga/
   - Detail warga: http://127.0.0.1:8000/warga/1/ (contoh)
   - Daftar pengaduan: http://127.0.0.1:8000/pengaduan/
   - Admin: http://127.0.0.1:8000/admin/  (buat superuser jika perlu `python manage.py createsuperuser`)

---

Jika kamu mau, aku bisa:
- Tambahkan file `.gitignore` yang cocok untuk Django
- Buat skrip/command untuk otomatis migrasi + loaddata
- (Opsional) Buatkan superuser default (tapi tidak disertakan demi keamanan)
