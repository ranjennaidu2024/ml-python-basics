# clean code
def is_even(num):
    # if even number , remainder will be 0
    if num % 2 == 0:
        return True
    else:
        return False


print(is_even(51))


# can make it shorter
# it's going to go line 17 if the statement incorrect
def is_even(num):
    if num % 2 == 0:
        return True
    return False


print(is_even(51))


# we just return true , false so there is better way , get exact same result , cleaner
def is_even(num):
    # this is a expression that going to evaluate to True False directly
    return num % 2 == 0


print(is_even(51))
