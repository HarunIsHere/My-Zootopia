import os
import requests

BASE_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {
        ...
      },
      'locations': [
        ...
      ],
      'characteristics': {
        ...
      }
    },
    """
    api_key = os.getenv("API_NINJAS_KEY")
    if not api_key:
        raise SystemExit("Missing API_NINJAS_KEY env var")

    response = requests.get(
        BASE_URL,
        headers={"X-Api-Key": api_key},
        params={"name": animal_name},
        timeout=15,
    )

    if response.status_code != 200:
        raise RuntimeError(f"API error {response.status_code}: {response.text}")

    return response.json()
