import requests
import time

MAX_RETRIES = 5
RETRY_DELAY = 5  # seconds

for attempt in range(1, MAX_RETRIES + 1):
    try:
        r = requests.get("http://backend:5000/")
        if r.status_code == 200:
            exit(0)  # Success
    except Exception as e:
        if attempt < MAX_RETRIES:
            time.sleep(RETRY_DELAY)
        else:
            exit(1)  # Failure
