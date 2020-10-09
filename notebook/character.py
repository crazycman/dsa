import json


class Character:
    def __init__(self, name, alter, aussehen, beschreibung):
        self.name = name
        self.alter = alter
        self.aussehen = aussehen
        self.beschreibung = beschreibung

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)

    def __repr__(self):
        return '\n{}, {}, {}, \n{}'.format(self.name, self.alter, self.aussehen, self.beschreibung)

# some_json = '''{
#     "name" : "Bolzo Trump",
#     "alter" : 19,
#     "aussehen" : "komisch",
#     "beschreibung" : "Taschendieb im Hafen"
#   }'''
#
# bolzo = Character.from_json(some_json)
# print(bolzo)
#
# all_characters = []
# with open('characters.json', 'r') as characters_file:
#     character = json.loads(characters_file.read())
#     for c in character:
#         all_characters.append(Character(**c))
#
# print(all_characters)