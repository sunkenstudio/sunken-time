import json
import os

def read_json(filename: str) -> dict:
    with open(filename) as file:
        d = json.load(file)
        file.close()
        return d

def write_json(filename: str, values: dict) -> None:
    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(values, file, indent=4)
        file.close()