# Type conversion - converting data types
# convert 100 integer into string
print(type(str(100)))

a = str(100)
b = int(a)
c = type(b)
print(c)

# similar to this
print(type(int(str(100))))
