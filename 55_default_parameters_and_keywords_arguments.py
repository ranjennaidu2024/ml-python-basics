# Default Parameters - define what you want as default for function , call the function even it's called wrong way
def say_hello(name='Dath Vader', emoji=':('):
    print(f'hello {name} {emoji}')


# Positional Arguments - because position matters , require to be in proper position - FOLLOW THIS PRACTICE - clean
say_hello('Andrei', ':)')

# Keyword Arguments - dont have to worry about position - BAD PRACTICE
# say_hello(emoji=':)',name='Bibi')
# if need to use for readability still follow the position
say_hello(name='Bibi',emoji=':)')

# using default parameters - without any arguments
say_hello()

# if we print the name param only , the emoji value will get from the default param
say_hello('Ranjen')