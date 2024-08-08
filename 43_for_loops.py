# variable item , can name to anything
for item in 'Zero to Mastery':
    # print each char in the strings
    print(item)
print('Done with loop')

# work the same with list,tuple and set as well
for item1 in [1, 2, 3, 4, 5]:
    # print each char in the strings
    print(item1)

for item2 in {1, 2, 3, 4, 5}:
    # print each char in the strings
    print(item2)

# nested loop - complete the second loop then continue with the first loop again
for my_item in [1, 2, 3, 4, 5]:
    for x in ['a', 'b', 'c']:
        print(my_item, x)
# 1a,1b,1c,2a,2b,2c,etc
