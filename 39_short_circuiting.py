# Short Circuiting
is_Friend = True
is_User = False

if is_Friend or is_User:
    print('best friend forever')

# Short circuit is used for or above coz as long is_Friend is true I don't care about the is_User , will print somehow

is_Friend = False
is_User = True

if is_Friend and is_User:
    print('best friend forever')

# same for above , if one of them is_Friend already false so no need to check on is_User
