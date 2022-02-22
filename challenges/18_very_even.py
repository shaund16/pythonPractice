def is_very_even_number(n):
    while len(str(n)) > 1:
      n = sum(int(x) for x in str(n))
    return True if n % 2 == 0 else False
print(is_very_even_number(0))
print(is_very_even_number(4))
print(is_very_even_number(12))
print(is_very_even_number(22))
print(is_very_even_number(5))
print(is_very_even_number(45))
print(is_very_even_number(4554))




# number = 88 => returns false -> 8 + 8 = 16 -> 1 + 6 = 7 => 7 is odd 

# number = 222 => returns true -> 2 + 2 + 2 = 6 => 6 is even

# number = 5 => returns false

# number = 841 => returns true -> 8 + 4 + 1 = 13 -> 1 + 3 => 4 is even