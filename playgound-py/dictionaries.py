# Create dict

person = {
  'first_name': 'John',
  'last_name': 'Doe',
  'age': 30
}

# Use constructor 
# person2 = dict(first_name='Sara', last_name='Williams')

# Get value 
print(person['first_name'])

print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'

# Get dict keys
print(person.keys())

# Get dict items 
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Calgary'

# Remove Item
del(person['age'])
person.pop('phone')

# Clear 
person.clear()

# Get length
print(len(person2))

# List of dict 
people = [
  {'name': 'Eliana', 'age': 1},
  {'name': 'Melanie', 'age': 31}
]

print(people[1]['name'])

