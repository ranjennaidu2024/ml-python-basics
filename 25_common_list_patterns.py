basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
basket.sort()
basket.reverse()
# list slicing is like copy and create a new list
print(basket[:-1])
# so the basket list remain untouched by the slicing above
print(basket)

# generate list quickly from 1 to 100
print(range(1, 100))
# start from particular number , end at 99
print(list(range(1, 100)))
# start from index 0 , from 0-100
print(list(range(101)))

# join
sentence = ' '
# join create new item for us
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'JOJO'])
# join will join the string in the list with whichever infront of it
print(new_sentence)

# shorter way to join list of strings
new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'JOJO'])
# join will join the string in the list with whichever infront of it
print(new_sentence)