name =("Yash")
age = 21
area = 3.14
food = "Samosa"

print("DataType of of the variable name : ",type(name))
print("DataType of of the variable age : ",type(age))
print("DataType of of the variable area : ",type(area))

# Data Types in python : 

# ==> Numeric :- int, float, complex
# ==> Sequence Type :- string, list, tuple
# ==> Mapping Type :- dict
# ==> Boolean :- bool
# ==> Set Type :- set, frozenset
# ==> Binary Types :- bytes, bytearray, memoryview

# => Integeres
# => Float
# => Boolean :- True or False , T and F should be capital.

# => Complex 
v = 34j # imaginary number
print(type(v))

# => String :- you can make a string by using double quotes or single quotes.
# ord() is used to find ASCII value and chr() is used to convert the ASCII value into number.


a = 'Hello'
print(a[0])
print(a[4])

# String slicing :- cutting out a slice from string and this is also done using index values.
a = "Hello Yash"
print(a[6:10:1]) # print(a[6::1]) , gives same output as stopping by default at the end of string.
# [start, stop, steps]

print(a[::]) # this prints whole string as default start and stop points.
