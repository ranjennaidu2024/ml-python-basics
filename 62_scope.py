# Scope - what variables do I have access to ?

# Functional

total = 100

if True:
    x = 10


def some_func():
    total2 = 100


# global scope , can use inside conditional or function block
print(total)
# functional scope - accessible within function only
# print(total2)

# not within a function and accessible within same scope
print(x)
