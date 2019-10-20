pokemon_list = []
with open('nameslist.txt') as list_file:
    pokemon_file = list_file.readlines()
    for line in pokemon_file:
        name = line[:-1]
        pokemon_list.append(name)
    pokemon_list.append('pokemon')

name = input('Type the name you want to test: ')
print('testing...')
pokenames_list = []
new_name = ''

for pokemon in pokemon_list:
    split_name = list(name.lower())
    pkm_name_length = len(pokemon)
    for poke_letter in pokemon:
        if poke_letter in split_name:
            new_name+=poke_letter
            split_name.remove(poke_letter)

    new_name+=' '
    if new_name[:pkm_name_length] == pokemon:
        for char in split_name:
            new_name+=char
        pokenames_list.append(new_name)
    new_name = ''

print('results:')
for pokename in pokenames_list:
    print(pokename)
