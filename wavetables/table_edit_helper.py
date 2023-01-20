import json

new_data = {}

with open('tables.json') as jsonfile:
    old_table_data = json.load(jsonfile)

with open('slopes.json') as jsonfile:
    old_slope_data = json.load(jsonfile)

for slug, table in old_table_data.items():
    new_data[slug] = table
    attack_stack = old_slope_data[table["slopes"][0]]["samples"]
    release_stack = old_slope_data[table["slopes"][1]]["samples"]
    is_wildcard = False
    is_scanner = True
    for idx, slope in enumerate(attack_stack):
        attack = slope
        release = release_stack[idx]
        if release[1] < 25000:
            is_scanner = False
        if attack[-1] < 30000:
            is_wildcard = True

    if is_scanner:
        new_data[slug]["tags"].append("Scanner Slope")
        is_wildcard = False
    if is_wildcard:
        new_data[slug]["tags"].append("Cycle")
    elif not is_scanner:
        new_data[slug]["tags"].append("Slope Pair")


with open('tables.json', 'w') as jsonfile:
    json.dump(new_data, jsonfile, indent=4)
