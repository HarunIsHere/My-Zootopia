import os
import requests


def fetch_animals_data(animal_name):
    """Fetch animals JSON from API Ninjas Animals API."""
    api_key = os.getenv("API_NINJAS_KEY")
    if not api_key:
        raise SystemExit("Missing API_NINJAS_KEY env var")

    response = requests.get(
        "https://api.api-ninjas.com/v1/animals",
        headers={"X-Api-Key": api_key},
        params={"name": animal_name},
        timeout=15,
    )

    if response.status_code != 200:
        raise RuntimeError(f"API error {response.status_code}: {response.text}")

    return response.json()  # list


def load_template(file_path):
    """Loads an HTML template file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return handle.read()


def serialize_animal(animal):
    """Returns an HTML <li> card for one animal (only existing fields)."""
    name = animal.get("name")
    characteristics = animal.get("characteristics", {}) or {}
    diet = characteristics.get("diet")
    animal_type = characteristics.get("type")
    locations = animal.get("locations", []) or []
    first_location = locations[0] if locations else None

    parts = ['<li class="cards__item">\n']

    if name:
        parts.append(f'  <div class="card__title">{name}</div>\n')

    parts.append('  <p class="card__text">\n')

    if diet:
        parts.append(f'      <strong>Diet:</strong> {diet}<br/>\n')
    if first_location:
        parts.append(f'      <strong>Location:</strong> {first_location}<br/>\n')
    if animal_type:
        parts.append(f'      <strong>Type:</strong> {animal_type}<br/>\n')

    parts.append('  </p>\n')
    parts.append('</li>\n')

    return "".join(parts)


def main():
    animal_name = input("Enter an animal name: ").strip()
    animals_data = fetch_animals_data(animal_name)

    template = load_template("animals_template.html")

    cards = []
    for animal in animals_data:
        cards.append(serialize_animal(animal))

    # If no results, render a single "no animals" card (keeps the HTML structure valid)
    if not cards:
        cards.append(
            '<li class="cards__item">\n'
            '  <div class="card__title">No animals found.</div>\n'
            '  <p class="card__text">Try a different search.</p>\n'
            '</li>\n'
        )

    output = "".join(cards)
    new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w", encoding="utf-8") as handle:
        handle.write(new_html)


if __name__ == "__main__":
    main()