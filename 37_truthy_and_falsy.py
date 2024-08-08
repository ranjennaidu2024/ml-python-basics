# Turthy and Falsy , still valid in python as it automatically convert to bool
is_old = 'hello'
is_licensed = 5

# This will give True
print(bool('hello'))
print(bool(5))

# This will give False , for more can google and chacke Python Falsy values
print(bool(''))
print(bool(0))
print(bool(None))

username = 'johnny'
password = '123'

# using truthy and falsy to execute as long the username and password value is there
if username and password:
    print('Logged in')
else:
    print('Invalid Login')