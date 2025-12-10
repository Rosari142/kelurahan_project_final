import requests

TOKEN = "528fddbf88804180dfd7fbbb7afded6b877de5e8"

url = "http://127.0.0.1:8000/api/v1/warga/"

headers = {
    "Authorization": f"Token {TOKEN}"
}

response = requests.get(url, headers=headers)

print("Status:", response.status_code)
print("Data:", response.json())
