# loop through this picture and whenever there is 0 print space and whenever there is 1 print *

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

# iterate over picture
# if 0 -> print ''

for row in picture:
    for pixel in row:
        if (pixel == 1):
            print('*', end='')
        else:
            print(' ', end='')
    # for each row it should go to new line , default \n
    print('')

# we can make it shorter using truthy and falsy , without bracket
for row in picture:
    for pixel in row:
        if pixel:
            print('*', end='')
        else:
            print(' ', end='')
    # for each row it should go to new line , default \n
    print('')

# everytime print will give new line , so can use the end param in print , by default it use \n if click the print and see

