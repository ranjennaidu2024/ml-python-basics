# Formatted Strings

name = 'Johny'
age = 55
print('hi ' + name + '. You are ' + str(age) + ' years old')

# From python 3 onwards - recommended , nice and clean
# Add f at beginning for formatted strings
print(f'hi {name}. You are {age} years old')

# For python 2 can use .format
print('hi {}. You are {} years old'.format('Johny','55'))
print('hi {}. You are {} years old'.format(name,age))
# can change the order too
print('hi {1}. You are {0} years old'.format(name,age))
# can create own variable if wanted
print('hi {new_name}. You are {age} years old'.format(new_name='sally',age=100))