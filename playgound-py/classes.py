class User:
 def __init__(self, name, email, age):
   self.name = name
   self.email = email
   self.age = age
   
def greeting(self):
  return (f'My name is {self.name} and I am {self.age}')

def has_birthday(self):
  self.age += 1

   
# Init user object
shaun = User('Shaun Daniel', 'shaun@gmail', '31')
shaun.has_birthday()
print(shaun.greeting())