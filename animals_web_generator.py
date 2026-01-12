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
    """Returns an HTML <li> block for one animal (only existing fields)."""
    parts = ['<li class="cards__item">']

    name = animal.get("name")
    if name:
        parts.append(f"Name: {name}<br/>\n")

    characteristics = animal.get("characteristics", {}) or {}
    diet = characteristics.get("diet")
    if diet:
        parts.append(f"Diet: {diet}<br/>\n")

    locations = animal.get("locations", []) or []
    if locations:
        parts.append(f"Location: {locations[0]}<br/>\n")

    animal_type = characteristics.get("type")
    if animal_type:
        parts.append(f"Type: {animal_type}<br/>\n")

    parts.append("</li>\n")
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