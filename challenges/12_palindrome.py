def is_palindrome(s):
    return s.lower() == s[::-1].lower()


print(is_palindrome("a"))
print(is_palindrome("aba"))
print(is_palindrome("Abba"))
print(is_palindrome("malam"))
print(is_palindrome("walter"))
