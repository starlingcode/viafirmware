import json

new_data = {}


with open('../meta/original.json') as jsonfile:
    meta_slugs = json.load(jsonfile)['slug_list']

with open('../sync/original.json') as jsonfile:
    sync_slugs = json.load(jsonfile)['slug_list']

with open('../scanner/original.json') as jsonfile:
    scanner_slugs = json.load(jsonfile)['slug_list']

with open('tables.json') as jsonfile:
    old_data = json.load(jsonfile)
    for thing in old_data:
        new_data[thing] = {}
        new_data[thing]['title'] = thing
        new_data[thing]['slopes'] = old_data[thing]
        if thing in meta_slugs:
            new_data[thing]['meta_default_index'] = meta_slugs.index(thing)
        else: 
            new_data[thing]['meta_default_index'] = -1
        if thing in sync_slugs:
            new_data[thing]['sync_default_index'] = sync_slugs.index(thing)
        else: 
            new_data[thing]['sync_default_index'] = -1
        if thing in scanner_slugs:
            new_data[thing]['scanner_default_index'] = scanner_slugs.index(thing)
        else: 
            new_data[thing]['scanner_default_index'] = -1

with open('tables.json', 'w') as jsonfile:
    json.dump(new_data, jsonfile)
