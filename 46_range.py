# range() - return object that produce sequence of integer from start to stop

print(range(100))

# iterate over range
for number in range(0,10):
    print(number)

# if you don't care about the variable we can just use _
for _ in range(0,10):
    print(_)

# third param - step forward 2
for _ in range(0,10,2):
    print(_)

# if want to do in reverse with 2 step
for _ in range(10,0,-2):
    print(_)

# a quick to way to create list of integers as many times we need
for _ in range(2):
    print(list(range(10)))