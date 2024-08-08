# list unpacking
basket = [1, 2, 3]

# assign variable to each item
# a, b, c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # print(a)
# # print(b)
# # print(c)

# what if we want to unpack 1,2,3 from list and keep the remaining
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)
# d will be the very last item of the list
print(d)
