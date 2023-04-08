import json

with open('private.json') as f:
    obj = json.load(f)
    print(obj['apikey'])

    