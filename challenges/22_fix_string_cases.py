def solve(s):
    upper = 0
    lower = 0
    for letter in s:
        if letter.isupper():
            upper += 1
        else:
            lower += 1

    return s.lower() if upper == lower or lower > upper else s.upper()


print(solve('code'))
print(solve('CODe'))
print(solve('COde'))
print(solve('Code'))
