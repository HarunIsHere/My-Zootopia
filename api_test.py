import os
import requests

API_KEY = os.getenv("API_NINJAS_KEY")
if not API_KEY:
    raise SystemExit("Missing API_NINJAS_KEY env var")

resp = requests.get(
    "https://api.api-ninjas.com/v1/animals",
    headers={"X-Api-Key": API_KEY},
    params={"name": "asdkfjhasdkj"},
    timeout=15,
)

print("Status:", resp.status_code)
print(resp.json() if resp.status_code == 200 else resp.text)
