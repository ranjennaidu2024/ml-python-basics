a = 1


def confusion():
    a = 5
    return a


print(confusion())  # give 5 as it get from the function scope , creating the 'a' within the function only
print(a)  # give 1 take from global scope


def parent():
    a = 10

    def confusion():
        return a

    return confusion()


# rules
# 1 - start with local scope
# 2 - Parent local ?
print(parent())  # print 10


# 3 - Global
# 4 - buil in python functions like sum which is built-in function
def parent():
    a = 10

    def confusion():
        return sum

    return confusion()


print(a)  # print 1
