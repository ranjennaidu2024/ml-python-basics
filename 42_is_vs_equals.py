print(True == 1) # True , 1 is converted as booleans which is true
print('' == 1) # False , '' is Falsy
print('1' == 1) # False , as we compare two types string vs int , not getting converted into boolean
print([] == 1) # False, [] is Falsy
print(10 == 10.0) # True
print([] == []) # True
print([1,2,3] == [1,2,3]) # True
print([1,2,3] == [1]) # False
# == check for equality of value

# check the same using is , get all False
# is - check if location in memory where value is stored is the same
print("--------------using Is--------------")
# print(True is 1)
# print('' is 1)
# print('1' is 1)
# print([] is 1)
# print(10 is 10.0)
# print([] is [])
# print([1,2,3] is [1,2,3])
# print([1,2,3] is [1])
# == check for equality of value

# to make it true for is
# string and integer use same memory space
print(True is True)
# print('1' is '1')
print([] is []) # return false as datastructure create different memory space
a = 1
b = 1
print(a is b)

c = [1,2,3]
d = [1,2,3]
print(c is d) # return false as datastructure create different memory space
print(c == d) # return true coz double equality only check the value