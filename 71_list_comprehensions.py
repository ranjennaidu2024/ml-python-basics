# list/set/dictionary comprehensions
# can use comprehension with three data type
# comprehensions - quick way to create list/set/dictionary instead of looping/appending bunch of items to list

my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

# there is cleaner and faster way to do above using comprehensions
my_list2 = [char for char in 'hello']
print(my_list2)

# quick list for number ranging from 0-100
my_number = [num for num in range(0,100)]
print(my_number)

# wanted each number range from 0-100 multiplied by two
# instead of use num just as variable we use it as expression, how to act upon each character
my_number2 = [num*2 for num in range(0,100)]
print(my_number2)

# keep power of 2 numbers range from 0-100
my_number3 = [num**2 for num in range(0,100)]
print(my_number3)

# wanted each number range from 0-100 multiplied by two but this time keep only even numbers
# we have option to add condition, to add into the list based on that condition
# make code shorter and cleaner but may be take time for readability (fix: add descriptive function name)
my_number4 = [num**2 for num in range(0,100) if num % 2 == 0]
print(my_number4)
