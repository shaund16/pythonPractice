def well(x):
  c = x.count('good')
  return 'I smell a series' if c > 2 else 'Publish!' if c else 'Fail!'

print(well(['bad', 'bad', 'bad']))
print(well(['good', 'bad', 'bad', 'bad', 'bad']))
print(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']))
print(well(['bad', 'bad', 'bad','bad', 'bad', 'bad']))
