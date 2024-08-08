# Python List Methods Ref: https://www.w3schools.com/python/python_ref_list.asp

basket = [1,2,3,4,5]

# calculate length of list
print(len(basket))

# for all below new_list, it just modify the one basket list in the memory and didn't create new one

# adding
new_list = basket.append(100)
print(basket)
# this does not return the value , just change the list so will give None
print(new_list)

# insert
# add 100 at the index of 4
new_list = basket.insert(4,100)
print(basket)

# extend - take iterator , where you can loop over , which is a list
new_list = basket.extend([100,101])
print(basket)


# removing can use pop or remove
# pop - give index we want to remove
# pop of whichever end of the list
basket.pop()
basket.pop()
# pop can also remove specific index , remove index 2 which is 3
basket.pop(2)
print(basket)

# remove - give value we want to remove , remove position value 2 which is 2
new_list = basket.remove(2)
print(new_list) # for remove will give None

# But for pop it will return a value that you just removed
new_list = basket.pop(3) # will return 5 from [1, 4, 100, 5, 100]
print(new_list)

# clear - to empty the list/basket
new_list = basket.clear()
print(basket) # removes whatever in list , completely clear it

# check each method which value it return , for insert,extend,remove all we can see None is returned when mouseover


