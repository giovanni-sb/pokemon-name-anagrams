import json

nameslist = []

with open('pokes.json') as json_file:
    data = json.load(json_file)
    for pokemon in data['results']:
        nameslist.append(pokemon['name'])

with open('nameslist.txt', 'w') as list_file:
    list_file.writelines("%s\n" % name for name in nameslist)