name = 'Ranjen'
age = 50
relationship_status = 'single'

relationship_status = 'it\'s complicated'

print(relationship_status)

birth_year = input('what year were you born?')

# that input will be converted to string , so need to turn it into integer to avoid type error
type(birth_year)

age = 2023 - int(birth_year)

print(f'Your age is: {age}')
