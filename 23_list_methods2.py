basket = ['a','b','c','d','e']

# get index of element
print(basket.index('d'))

# optional param where should start and stop looking at index , start at index 0 and 2 will give error
# print(basket.index('d', 0, 3))
print(basket.index('d', 0, 4))

# another better way to look in list
print('d' in basket)
print('f' in basket)

# in can be also use for string
print('i' in 'ranjen nadu')

# count how many times that item occur
basket = ['a','b','c','d','e', 'd']
print(basket.count('d'))