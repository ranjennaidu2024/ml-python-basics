# enumerate - use if need index counter of the item you looping through
# return an enumarate object , with item and index

for char in enumerate('Hello'):
    print(char)

for i,char in enumerate('Hello'):
    print(i,char)

# so using this we can get the index together with item , same with tuple
for i,char in enumerate([1,2,3]):
    print(i,char)

# to get and print only the index of number 50
for i,char in enumerate(list(range(100))):
    # print(i, char)
    if char==50:
        print(f'Index of 50 is {i}')