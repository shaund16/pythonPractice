def evens_and_odds(n):
    return format(n, 'b') if n % 2 == 0 else hex(n)[2:]


print(evens_and_odds(2))  # '10'
print(evens_and_odds(13))  # 'd'
