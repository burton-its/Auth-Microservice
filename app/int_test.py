import requests

AUTH_URL = "http://127.0.0.1:8000"
FILE_URL = "http://127.0.0.1:8002"

EMAIL = "test7@example.com"
PASSWORD = "securepass123"

# register
requests.post(
    f"{AUTH_URL}/auth/register",
    json={"email": EMAIL, "password": PASSWORD}
)

# login and get the token
login_response = requests.post(
    f"{AUTH_URL}/auth/login",
    json={"email": EMAIL, "password": PASSWORD}
)

token = login_response.json()["access_token"]
print("got the token")

# set up the download
file_response = requests.post(
    f"{FILE_URL}/file-download",
    json={
        "title": "test_export",
        "filetype": "CSV",
        "data": [
            {"name": "Corey", "age": 30},
            {"name": "Finn", "age": 29},
        ],
    },
    headers={"Authorization": f"Bearer {token}"}
)

# save file
with open("output.csv", "wb") as f:
    f.write(file_response.content)

print("File saved as output.csv")