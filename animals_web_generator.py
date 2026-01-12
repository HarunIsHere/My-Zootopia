import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def main():
    animals_data = load_data("animals_data.json")

    for animal in animals_data:
        name = animal.get("name")
        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet")
        animal_type = characteristics.get("type")
        locations = animal.get("locations", [])
        first_location = locations[0] if locations else None

        if name:
            print(f"Name: {name}")
        if diet:
            print(f"Diet: {diet}")
        if first_location:
            print(f"Location: {first_location}")
        if animal_type:
            print(f"Type: {animal_type}")

        print()  # blank line between animals


if __name__ == "__main__":
    main()