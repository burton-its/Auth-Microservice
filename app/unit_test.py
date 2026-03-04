# http client library
import requests

AUTH_URL = "http://127.0.0.1:8000"
EMAIL = "test13@example.com"
PASSWORD = "test13"

# register
requests.post(f"{AUTH_URL}/auth/register", json={"email": EMAIL, "password": PASSWORD})

# login
r = requests.post(f"{AUTH_URL}/auth/login", json={"email": EMAIL, "password": PASSWORD})
r.raise_for_status()

# show that we get the token
token = r.json()["access_token"]
print("JWT:", token)
