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

# common functions : int() , float(), str(), bool()