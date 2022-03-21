def center(string, width, fill=" "):
    width -= len(string)
    right = width // 2
    left = width - right
    return "{}{}{}".format(left * fill, string, right * fill)


print(center("a", 3))
print(center("abc", 10, "_"))
print(center("abcdefg", 2))
