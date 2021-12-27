# String Formatting 

name = 'Shaun'
age = 31

# Concatenate 

print('Hello, my name is ' + name + ' and I am ' + str(age))


# String Formatting 


# Arguments by Position
print('My name is {name} and I am {age}'.format(name=name, age=age))


# String Methods

s = 'hello world' 

# Capitalize String
print(s.capitalize())

#Make all upperCase
print(s.upper())

#Make all lower 
print(s.lower())

#Swap Case
print(s.swapcase());

#Get Length
print(len(s));

# Replace
print(s.replace('world', 'everyone'))

