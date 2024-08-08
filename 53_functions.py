# functions
# def is shortform for define

def say_hello():
    print('hello')


# in order to use the function , we need to call with bracket
say_hello()

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]


# if put above the function declaration it wont work as interpreter go line by line, define the function in the beginning
# show_tree()
def show_tree():
    for row in picture:
        for pixel in row:
            if pixel:
                print('*', end='')
            else:
                print(' ', end='')
        print('')


# able to do the same thing over and over by just calling the functions
show_tree()
show_tree()
show_tree()

# print the function name without bracket will give the location in memory
print(show_tree)


