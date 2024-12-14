import json

def read_json(filename: str) -> dict:
    with open(filename) as file:
        d = json.load(file)
        file.close()
        return d

def write_json(filename: str, values: dict) -> None:
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(values, file, indent=4)
        file.close()