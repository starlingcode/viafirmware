import json

new_data = {}

with open('tables.json') as jsonfile:
    old_data = json.load(jsonfile)
    for thing in old_data:
        new_data[thing] = old_data[thing]
        new_data[thing]['desription'] = "Describe meeeeeeeee"

with open('tables.json', 'w') as jsonfile:
    json.dump(new_data, jsonfile)
