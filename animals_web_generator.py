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


def get_serialized_animal_data(animal_data):
    text = '<li class="cards__item">\n'
    name = animal_data.get("name", None)
    if name:
        text += f'<div class="card__title">{name}</div>\n'
    locations = animal_data.get("locations", None)
    text += '<p class="card__text">\n'
    if locations:
        text += f"<strong>Location</strong>: {locations[0]}<br/>\n"
    characteristics = animal_data.get("characteristics", None)
    if characteristics:
        diet = characteristics.get("diet", None)
        if diet:
            text += f"<strong>Diet</strong>: {diet}<br/>\n"
        animal_type = characteristics.get("type", None)
        if animal_type:
            text += f"<strong>Type</strong>: {animal_type}<br/>\n"
    text += '</p>\n</li>\n'
    return text


def get_animals_html(animals_data):
    animal_texts = []
    for animal in animals_data:
        text = get_serialized_animal_data(animal)
        animal_texts.append(text)
    return "\n".join(animal_texts)


def main():
    animals_data = load_data("animals_data.json")

    animals_text = get_animals_html(animals_data)

    template_text = load_file("animals_template.html")

    updated_template = template_text.replace(
        "__REPLACE_ANIMALS_INFO__",
        animals_text,
    )

    write_file("animals_template.html", updated_template)

if __name__ == "__main__":
    main()
