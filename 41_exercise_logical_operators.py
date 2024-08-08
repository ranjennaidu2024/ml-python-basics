is_magician = False
is_expert = True

# check if magician and expert:
# "you are a master magician"

# check if magician but not expert:
#"at least you're getting there"

# if you're not magician:
# "you need magic powers"

if is_expert and is_magician:
    print("you are a master magician")
elif is_magician and not is_expert:
    print("at least you're getting there")
elif not is_magician:
    print("you need magic powers")
