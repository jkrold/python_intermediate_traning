import json


class Human:
    def __init__(self, age, name, surname):
        self.age = age
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Human: {self.name} {self.surname}, {self.age}"

    def convert_to_dict(self):
        return self.__dict__

def json_human_to_file(humans: list):
    humans_serialize = []

    for human in humans:
        human_dict = human.convert_to_dict()
        human_json = json.dumps(human_dict)
        humans_serialize.append(human_json)

    try:
        with open("./humans.json", "w") as fd:
            json.dump(humans_serialize, fd, indent=2)
    except (IOError, Exception) as e:
        print(f'Problem with writing to file, more info: {e.args}')