# 1.break keyword work in forloop as well

my_list = [1, 2, 3]

for item in my_list:
    print(item)
    break

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    break

# 2. besides break, we can use continue , it wont print as it keep going the loop if use continue

for item in my_list:
    continue
    print(item)

i = 0
while i < len(my_list):
    i += 1
    continue
    print(my_list[i])

# 3. pass is not very useful , does nothing
for item in my_list:
    pass
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    pass

# but can be used as placeholder - when you don't know what to do , still thinking
for item in my_list:
    # thinking about it , so can add pass here to continue the for loop , so don't bug us
    pass


