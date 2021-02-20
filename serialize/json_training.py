import json


def json_to_file():
    json_list = [
        {"name": "John"},
        {"name": "Anna"}
    ]

    try:
        with open("./training.json", "w") as fd:
            json.dump(json_list, fd, indent=2)
    except (IOError, Exception) as e:
        print(f'Problem with writing to file, more info: {e.args}')
