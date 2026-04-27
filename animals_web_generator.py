import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')

for animal in animals_data:
    text = ""
    name = animal.get("name", None)
    if name:
        text += "Name: " + name + "\n"
    locations = animal.get("locations", None)
    if locations:
        text += "Location: " + locations[0] + "\n"
    characteristics = animal.get("characteristics", None)
    if characteristics:
        diet = characteristics.get("diet", None)
        if diet:
            text += "Diet: " + diet + "\n"
        animal_type = characteristics.get("type", None)
        if animal_type:
            text += "Type: " + animal_type + "\n"
    text = text
    print(text)
