dictionary = { 'name':'Dario', 'age': 20 }

print(dictionary['name'])
print(dictionary['age'])

dictionary['name'] = 'Pablito'

print(dictionary)


dictionary['test'] = {'last_name':'Moreno'}

print(dictionary['test'])
print(dictionary['test']['last_name'])

print(dictionary.keys())

print(dictionary.values())

