def remove(s):
    return s[:-1] if s.endswith('!') else s


print(remove("Hi!"))
print(remove("Hi!!!"))
print(remove("!Hi!"))
print(remove("Hi! Hi!"))
