# list is like array -  is ordered sequence of object
li = [1,2,3,4,5]
li2 = ['a','b','c']
# can mix
li3 = [1,2,'a','b',True]

# Data structure - way to organize data into folder/box to be used
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]
print(amazon_cart[1])

# List slicing
# get item from first to second using slice
print(amazon_cart[0:2])

# List are mutable - can replace with other value
amazon_cart[0] = 'laptop'
print(amazon_cart)

# with list slicing we create new copy of the list
print(amazon_cart[0:2])

# instead of slicing we assign amazon_cart to new_cart
# new_cart = amazon_cart
# so if you want to copy we need to use [:]
new_cart = amazon_cart[:]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)