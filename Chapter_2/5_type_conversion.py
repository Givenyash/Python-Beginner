# These are of two types : implicit (automatic) and explicit (manual)

# Implicit conversion
x = 5   #int
y = 2.5    #float
z = x + y   #python converts int --> float
print (z)

# Explicit conversion
x = "10"   #string
y = int(x)  #str --> int
print(y+5)   # output: 15

# common type conversion functions : int(), float(), str(), bool()
# others are : complex(), list(), tuple(), set(), dict()

# to convert from one to another dataType

# Falsy values (7) : 
# 0
# 0.0
# " " empty string
# [ ] empty list
# ( ) empty tupple
# { } empty dictionary