# Operators perform operations on variable and values.
# types of operator : Arithmetic , Comparison , Logical, Assignment, Bitwise

#Example
x = 5
y = 3
print(x + y)
print( x > y)
print ( x > 0 and y < 20)

#Arithmatic operators
print()
print("Arithmatic operators")
x=10
y=6

print("Sum:",x+y)
print("Difference:",x-y)
print("Product:",x*y)
print("Divison:",x/y)
print("Modulus:",x%y)
print("Power:", x**y)

print()

print("Comparison operators")
#Comparison operators

print("Equality:",x==y)
print("Greater than or equal to :",x>=y)
print("Less than or equal to :",x<=y)
print("x is greater than y :",x>y)
print("y is greater than x :",x<y)
print("x is not equal to y :",x!=y)

print()

print("Logical operator")

#Logical operator

print("AND operator :",x>y and y<10)
print("OR operator :" , x<y or y < 10)
print("NOT operator :",not(x>y))

print()

print("Assignment operator")

#Assignment operator

a = 2
b = 3

a=a+6
a+=6

a=a-1
a-=1

a=a/10
a/=10

a=a*10
a*=10