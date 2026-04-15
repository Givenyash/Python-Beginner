# Operators perform operations on variable and values.
# types of operator : Arithmetic , Comparison , Logical, Assignment, Bitwise
# Python follows BODMAS Rule

#Arithmatic operators : perform mathematical operations
print()
print("Arithmatic operators")
x=10
y=5

print("Sum:", x + y) # (+)
print("Difference:", x - y) # (-)
print("Product:", x * y) # (*)
print("Divison:", x / y) # (/)
print("Modulus:", x % y) # (%)
print("Power:", x ** y) # (**)

print(x / y) # output => 2.0
print(x // y) # output => 2 , this is called floor division , it results in integer.

print()


print("Comparison operators")
#Comparison operators : These are also called relational operators and are used to compare two values. This will always provide Boolean result. A comparison btw a string and a number can't possible.

print("Equality:",x == y) # (==)
print("Greater than or equal to :", x >= y) # (>=)
print("Less than or equal to :", x <= y) # (<=)
print("x is greater than y :", x > y) # (>)
print("y is greater than x :", x < y) # (<)
print("x is not equal to y :", x != y) # (!=)
# They will work with numsbers but we can use them with strings as well. Strings will be compared through their ASCII values.

print()


print("Logical operator")
#Logical operator : These are used in Python to combine multiple conditions and return a Boolean result.

print("AND operator :",x > y and y < 10) # return true if both conditions are true, else false
print("OR operator :" , x < y or y < 10) # return true when one or more of the condition is true
print("NOT operator :",not(x > y)) # reverse the boolean value

print()


print("Assignment operator")
#Assignment operator : These are the operators used to assign values to variables.

a = 2 # just assign
a+=6 # Add & assign
a-=1 # Substract & assign
a/=10 # Divide and assign
a*=10 # Multiply and assign
a%=2 # modulus and assign  
a//=10 # Floor divide and assign
a**= 5 # Exponentiation and assign
print(a)