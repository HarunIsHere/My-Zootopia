import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


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
    animals_data = load_data("animals_data.json")
    template = load_template("animals_template.html")

    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)

    new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w", encoding="utf-8") as handle:
        handle.write(new_html)


if __name__ == "__main__":
    main()