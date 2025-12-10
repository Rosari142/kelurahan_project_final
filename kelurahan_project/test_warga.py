import requests

url = "http://127.0.0.1:8000/api/v1/warga/"
token = "528fddbf88804180dfd7fbbb7afded6b877de5e8"

headers = {
    "Authorization": f"Token {token}"
}

res = requests.get(url, headers=headers)
print(res.status_code)
print(res.json())
