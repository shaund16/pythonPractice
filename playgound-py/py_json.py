import json 

# Sample JSON 
userJSON = '{"first_name": "John", "last_name": "Doe",}'

# Parse to dict 
user = json.loads(userJSON)

print(user)