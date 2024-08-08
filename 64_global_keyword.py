# Global Keyword

# parameter is part of local scope, parameter are consired as local variable , it is within function

a = 10


def confusion(b):
    print(b)
    a = 90


confusion(300)

# if let say you wanted to refer the 'a' in local scope to your 'a' in global scope
total = 0


def count():
    # using total but we haven't assign anything yet
    # we want the total from outside world to run
    # total += 1
    # so we use the global keyword , to use the total from global scope
    global total
    total += 1
    return total


count()
count()
print(count())

# the above is not recommended , it is simplified version , complicated as it getting bigger and bigger
# the best approach is to use the dependency injection as below
# detach the count variable have with the outside global scope
total2 = 0


def count(total2):
    total2 += 1
    return total2


print(count(count(count(total2))))
