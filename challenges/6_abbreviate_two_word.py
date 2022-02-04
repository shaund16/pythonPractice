def abbrev_name(name):
  first, last = name.upper().split(' ')
  return first[0] + '.' + last[0]


print(abbrev_name("Sam Harris"))
print(abbrev_name("patrick feenan"))
print(abbrev_name("Evan C"))
    