selfish = 'me me me'

print(selfish[0])

# [start:stop] - get from index 0 till 1
print(selfish[0:2])

# [start:stop:stepover] - get from index 0 till 7 with stepover 2
selfish2 = '01234567'
print(selfish2[0:8:2])

# start with 1 and default till end
print(selfish2[1:])
# start all the way till 5
print(selfish2[:5])
# start at zero when nothing , and end till 7 when nothing , step over with 1
print(selfish2[::1])

# negative means start at the end
print(selfish2[-2]) # will get 6
# step over from the back - we get reverse of the string
print(selfish2[::-1])
print(selfish2[::-2])

# this also known as slicing