# DocString - do unique thing with functions
# allow us to comment inside of the functions when we hover over

def test(a):
    '''
    Can add info about the function here
    :param a:
    :return:
    '''
    print(a)


test('!!!')

# also can use help pre-built function to see print the functions do
help(test)
# or other way is to use the dunder method
print(test.__doc__)