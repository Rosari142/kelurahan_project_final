import requests

# Token yang valid untuk autentikasi
TOKEN = "b8ae367dfc9fca9e6974c7f41debdd80d886aa6a"

# Header Authorization
HEADERS = {
    "Authorization": f"Token {TOKEN}"
}

# Daftar endpoint Django-mu
ENDPOINTS = {
    "List Warga": "http://127.0.0.1:8000/api/warga/",
}

def test_endpoints():
    for name, url in ENDPOINTS.items():
        try:
            response = requests.get(url, headers=HEADERS)
            print(f"\nEndpoint: {name}")
            print(f"URL: {url}")
            print(f"Status Code: {response.status_code}")
            print("Response JSON:", response.json())
        except Exception as e:
            print(f"Error accessing {url}: {e}")

if __name__ == "__main__":
    test_endpoints()

