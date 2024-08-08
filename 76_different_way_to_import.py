# shopping_cart is the module but shopping is the package
# instead of writing like this
# import test_packages.more_shopping.shopping_cart2
# print(test_packages.more_shopping.shopping_cart2.buy('orange'))

# we can make the import shorter by use from instead of import
# from <package_name> import <function_name>
from test_packages.more_shopping.shopping_cart2 import buy
# use coma for multiple functions

# import all the functions from that utility module using *
# from utility import *
# instead of above we can explicitly tell the required functions only so that we dont have to check the module again
from utility import multiply, divide, max

print(buy('orange'))
print(multiply(2, 2))
print(divide(10, 5))

# you also import the module instead of function
from test_packages.more_shopping import shopping_cart2

# if like that then can call the shopping_cart2 function like this
print(shopping_cart2.buy('grapes'))

# we overwrite the buit in max function with our utility module max function
print(max([1, 2, 3]))
