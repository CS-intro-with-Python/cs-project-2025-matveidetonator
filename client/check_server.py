import requests

try:
    r = requests.get("http://backend:5000/")
    print("Server response:", r.text)
except Exception as e:
    print("Error:", e)
    exit(1)
