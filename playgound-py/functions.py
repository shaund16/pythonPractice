# Create function 
def sayHello(name):
  print(f'Hello {name}')  
  
print(sayHello('Bob'))
 
 # Return values
def getSum(num1, num2):
  total = num1 + num2
  return total



getSum = lambda num1, num2 : num1 + num2

print(getSum(10, 3))