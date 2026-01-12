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
    """Returns a text block for one animal (only existing fields)."""
    lines = []

    name = animal.get("name")
    if name:
        lines.append(f"Name: {name}")

    characteristics = animal.get("characteristics", {}) or {}
    diet = characteristics.get("diet")
    if diet:
        lines.append(f"Diet: {diet}")

    locations = animal.get("locations", []) or []
    if locations:
        lines.append(f"Location: {locations[0]}")

    animal_type = characteristics.get("type")
    if animal_type:
        lines.append(f"Type: {animal_type}")

    return "\n".join(lines)


def main():
    animals_data = load_data("animals_data.json")
    template = load_template("animals_template.html")

    output = ""
    for animal in animals_data:
        block = serialize_animal(animal)
        if block:
            output += block + "\n\n"  # blank line between animals

    new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w", encoding="utf-8") as handle:
        handle.write(new_html)


if __name__ == "__main__":
    main()