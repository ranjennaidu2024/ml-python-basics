# while condition is happening do something

# while loop need to be careful can be infinite if didnt stop properly
i = 0
while 0 < 50:
    print(i)
    # fix for that is break keyword to stop the while loop
    break

# if want to loop for only 50 times
j = 0
while j < 50:
    print(j)
    j += 1 # each time will add one and will break the while loop once reached 50
    # j = j + 1

# can also have else clause for while loop , as soon as get last part print the else
# else will only execute if there was no break statement inside the loop
# use this only when there is no any break statement
k = 0
while k < 10:
    print(k)
    k += 1
else:
    print('done with all the work')


# else will only execute if there was no break statement inside the loop
# if have break it will break the whole while and else and go to the next line after that
# so will just print 0 and break without print the else statement
l = 0
while l < 5:
    print(l)
    l += 1
    break
else:
    print('done with all the work')