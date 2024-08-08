# calculate length of line - start from 1
print(len('hello'))

greet = 'hellloooo'
print(greet[0:len(greet)])

# string methods , methods that only string can perform
# Ref - https://www.w3schools.com/python/python_ref_string.asp

quote = 'to be or not to be'

# capatilize all letters
print(quote.upper())
print(quote.lower())
# capatilize beginning of each letter
print(quote.capitalize())

# check if exist or not in string using find
print(quote.find('be')) # return 3 to tell it is at index of 3

# replace
print(quote.replace('be','me'))

# strings a immutable , we create or destory them but can't change them. so the above just create new string
print(quote)