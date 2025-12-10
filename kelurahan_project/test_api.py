import requests

# ========================
# CONFIGURATION
# ========================
TOKEN = "b8ae367dfc9fca9e6974c7f41debdd80d886aa6a"
HEADERS = {
    "Authorization": f"Token {TOKEN}"
}
ENDPOINTS = {
    "List Warga": "http://127.0.0.1:8000/api/warga/",
}

# ========================
# FUNCTIONS
# ========================
def test_server():
    """Cek apakah server Django sedang berjalan"""
    try:
        r = requests.get("http://127.0.0.1:8000/")
        if r.status_code == 200 or r.status_code == 302:
            print("✅ Server Django berjalan!")
            return True
        else:
            print(f"⚠️ Server merespon tapi status code: {r.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Tidak bisa tersambung ke server! Pastikan 'python manage.py runserver' sudah dijalankan.")
        return False

def test_endpoints():
    """Cek semua endpoint dengan token"""
    for name, url in ENDPOINTS.items():
        try:
            response = requests.get(url, headers=HEADERS)
            print(f"\n📌 Endpoint: {name}")
            print(f"URL: {url}")
            print(f"Status Code: {response.status_code}")
            if response.status_code == 401:
                print("⚠️ Unauthorized — pastikan token benar!")
            else:
                try:
                    print("Response JSON:", response.json())
                except ValueError:
                    print("Response bukan JSON:", response.text)
        except Exception as e:
            print(f"Error accessing {url}: {e}")

# ========================
# MAIN
# ========================
if __name__ == "__main__":
    if test_server():
        test_endpoints()
