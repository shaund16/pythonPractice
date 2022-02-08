def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)
      
      
print(greet("James"))
print(greet("Jane"))
print(greet("Jim"))
print(greet("Johnny"))