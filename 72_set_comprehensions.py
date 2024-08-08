
simple_dict= {
    'a': 1,
    'b': 2
}
# {what we wanna do with data}
# extract the key and value using the dict.items to have to values , the value multiplied by 2
my_dict = {k:v**2 for k,v in simple_dict.items()}
print(my_dict)

# only to add when the value is even
my_dict2 = {k:v**2 for k,v in simple_dict.items() if v%2 == 0}
print(my_dict2)

# want to do for number in list 1,2,3 , item is the key and item * 2 is the value
my_dict2 = {num:num*2 for num in [1,2,3]}
print(my_dict2)