is_old = True
is_licensed = True

# need to indent to show that it is under the if statement
# Will ge true for first so ignore the rest
if is_old and is_licensed:
    print('You are old enough to drive!')
elif is_licensed:
    print('You can drive now')
else:
    print('you are not of age!')

print('okokok')