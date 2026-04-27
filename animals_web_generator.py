import json


def load_file(file_path):
    """ Loads a file """
    with open(file_path, "r", encoding="utf-8") as handle:
        return handle.read()


def write_file(file_path, data):
    """ Writes data to a file """
    with open(file_path, "w", encoding="utf-8") as handle:
        handle.write(data)


def load_data(file_path):
    """ Loads a JSON file """
    return json.loads(load_file(file_path))


def get_animals_text(animals_data):
    animal_texts = []
    for animal in animals_data:
        text = ""
        name = animal.get("name", None)
        if name:
            text += f"Name: {name}\n"
        locations = animal.get("locations", None)
        if locations:
            text += f"Location: {locations[0]}\n"
        characteristics = animal.get("characteristics", None)
        if characteristics:
            diet = characteristics.get("diet", None)
            if diet:
                text += f"Diet: {diet}\n"
            animal_type = characteristics.get("type", None)
            if animal_type:
                text += f"Type: {animal_type}\n"
        animal_texts.append(text)
    return "\n".join(animal_texts)


def main():
    animals_data = load_data("animals_data.json")

    animals_text = get_animals_text(animals_data)

    template_text = load_file("animals_template.html")

    updated_template = template_text.replace(
        "__REPLACE_ANIMALS_INFO__",
        animals_text,
    )

    write_file("animals_template.html", updated_template)

if __name__ == "__main__":
    main()
