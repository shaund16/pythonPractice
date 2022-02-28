def to_time(seconds):
    return f'{seconds//3600} hour(s) and {(seconds//60)%60} minute(s)'


print(to_time(3600))
print(to_time(3601))
print(to_time(3500))
print(to_time(323500))
print(to_time(0))
