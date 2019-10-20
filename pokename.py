pokemon_names_list = []
with open('nameslist.txt') as list_file:
    pokemon_file = list_file.readlines()
    for line in pokemon_file:
        pokemon = line[:-1]
        pokemon_names_list.append(pokemon)
    pokemon_names_list.append('pokemon')

#pokemon_names_list = ['pikachu', 'hypno', 'bulbasaur']

name_string = input('Type the name you want to test: ')
print('testing...')

def find_anagrams(name, pokemon_list):
    #print(name)
    results = []
    new_name = ''
    remainings = ''
    for pokemon in pokemon_list:
        split_name = list(name.lower())
        pkm_name_length = len(pokemon)
        for poke_letter in pokemon:
            if poke_letter in split_name:
                new_name+=poke_letter
                split_name.remove(poke_letter)
                #print(new_name+'<--'+str(split_name))
        new_name+=' '
        if new_name[:pkm_name_length] == pokemon:
            remainings = ''.join(split_name)
            more_names, remainings = find_anagrams(remainings, pokemon_list)
            if not more_names:
                results.append(new_name+remainings)
            else:
                for item in more_names:
                    results.append(new_name+item)
        else:
            remainings = name
        new_name = ''
    return results, remainings

pokenames, leftover = find_anagrams(name_string, pokemon_names_list)

print('results:')
for pokename in pokenames:
    print(pokename)
