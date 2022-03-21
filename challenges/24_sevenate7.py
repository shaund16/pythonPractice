def seven_ate9(str_):
    while str_.find("797") != -1:
        str_ = str_.replace("797", "77")
    return str_


print(seven_ate9("165561786121789797"))
print(seven_ate9("797"))
print(seven_ate9("7979797"))
