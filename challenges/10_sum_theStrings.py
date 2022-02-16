def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))
    
  
print(sum_str("4","5"))
print(sum_str("34","5"))
print(sum_str("","9"))
print(sum_str("8",""))
print(sum_str("",""))