# print the highest even from the list which is 10

def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print(highest_even([10, 2, 3, 4, 8, 11]))


