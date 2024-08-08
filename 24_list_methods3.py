basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
basket.sort()
print(basket)

basket2 = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
# using function sorted - produces new array
print(sorted(basket2))
# can see the basked hasn't been modified
print(basket2)

# same as this
# new_basket = basket2[:]
# instead of above we can use the copy method
new_basket = basket2.copy()
new_basket.sort()
print(new_basket)
print(basket2)

#  reverse - switching all the indexes into opposite site
basket2.reverse()
print(basket2)

# we can sort and reverse if needed
basket2.sort()
basket2.reverse()
print(basket2)