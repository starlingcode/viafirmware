import json

new_data = {}

with open('tables.json') as jsonfile:
    old_data = json.load(jsonfile)
    new_data = old_data
    for thing in old_data:
        old_data[thing]["tags"]

# with open('tables.json', 'w') as jsonfile:
#     json.dump(old_data, jsonfile, indent=4)
