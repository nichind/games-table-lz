import json

def getconfig() -> dict:
    with open('./config.json', 'r', encoding='UTF-8') as f:
        config = json.load(f)
    return config