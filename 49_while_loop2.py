my_list = [1, 2, 3]

# for simple loop for loop is great
# this my_list can be iterated with for or while loop
for item in my_list:
    print(item)

# if not sure how many times need to loop, how long it will loop,  use while loop
# flexible , can loop more than three times if needed , more powerful
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

# most useful way to do while loop is like this
# you don't know how long it's going to happen as long it met the condition
while True:
    response = input('say something: ')
    # it will keep asking till you say bye
    if (response == 'bye'):
        break
