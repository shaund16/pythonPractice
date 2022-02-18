def remove(s):
  return s.replace('!', '') + '!'
  
print(remove('Hi!'))
print(remove('Hi!!!'))
print(remove('!Hi'))
print(remove('!Hi!'))
print(remove('Hi! Hi!'))
print(remove('Hi'))