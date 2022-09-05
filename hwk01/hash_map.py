# The easiest way to implement a hash map in Python is through a dictionary
person_hash_map = {
    'full_name': 'Sebastian Andres Saldana Cardenas',
    'age': 22,
    'school': 'Tec de Monterrey'
}

# Access a key
print('The person\'s name is ', person_hash_map['full_name'])

# Add elements
person_hash_map['nickname'] = 'Sebas'
person_hash_map['school_id'] = 'A01570274'
print('Hash map after adding items \n', person_hash_map)

# Get the keys in a hash map
print('Hash map keys: \n', person_hash_map.keys())

# Get the values in a hash map
print('Hash map values: \n', person_hash_map.values())

# Iterate over the hash map 
print('Iterating over hash map')
for key in person_hash_map.keys():
    print('Key: ' + key + ' -- Value: ' + str(person_hash_map[key]))