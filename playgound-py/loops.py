people = ['John', 'Paul', 'Sara', 'Susan']

for person in people:
  print(f'Current Person: {person}')
  
  # Break 
  # for person in people:
  #   if person == 'John':
  #     break
  #   print(f'Current Person: {person}')
    
     # Continue  
  # for person in people:
  #   if person == 'Paul':
  #     continue
  #   print(f'Current Person: {person}')
  
  #range
  # for i in range(len(people)):
  #   print(people[i])
    
  # for i in range(0, 11):
  #   print(f'Number: {i}')
  
  count = 0
  while count <= 10:
    print(f'Count: {count}')
    count += 1