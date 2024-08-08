def sum(num1, num2):
    print('hi')
    num1 + num2


# nothing happens
sum(4, 5)

# this will print hi and None
# functions always have to return something or do one thing really well , if don't have return it will return None
print(sum(4, 5))


def sum(num1, num2):
    return num1 + num2


print(sum(6, 6))

# can assign to variables and call it
total = sum(10, 5)
print(sum(10, total))


def sum(num1, num2):
    def another_func(num1, num2):
        return num1 + num2


# print None as return is not under sum, we define another function but never call the function
total = sum(10, 20)
print(total)


# 1. To fix this we need to return the another_func
def sum(num1, num2):
    def another_func(num1, num2):
        return num1 + num2

    return another_func  # will return memomry location


# total is going to be equal to the another_func and will be stored in memory
total = sum(20, 20)
print(total(20, 20))


# 2. or like this
def sum(num1, num2):
    def another_func(num1, num2):
        return num1 + num2

    return another_func(num1, num2)  # will return actual value


total = sum(30, 20)
print(total)


# the above 1 and 2 not very good and confusing so change like this:
def sum(num1, num2):
    def another_func(n1, n2): # this is like defining and not running
        return n1 + n2

    return another_func(num1, num2)
    # return 5
    # return ('hello')


# to clarify when we return another_func function , we use the num1 and num2 parameter
total = sum(40, 40)
print(total)


# return keyword - automatically exit the functions , never get to line 66 and 67 above