def same_case(a, b):
  return a.isupper() == b.isupper() if a.isalpha() and b.isalpha() else -1
  
print(same_case('C', 'B')) 
print(same_case('b', 'a')) 
print(same_case('d', 'd')) 
print(same_case('A', 's'))