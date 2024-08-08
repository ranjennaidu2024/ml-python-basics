# nonlocal is new keyword in python3
# used to refer parent local - if want to use outside of local variable
# try to avoid nonlocal and global if possible to make your code clean

def outer():
    x = "local"

    def inner():
        nonlocal x  # referring to the parent x = 'local'
        x = "nonlocal"  # assigning this value to the parent x
        print('inner:', x)

    inner()
    print('outer:',
          x)  # we have modified the x outside with non-local keyword earlier, so this become non-local as well


outer()

# after we call the function above , python call garbage collector will empty the memory so other process can use that
# print(x) # cannot identify x
