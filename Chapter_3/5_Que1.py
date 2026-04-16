# Accept two numbers and print the greatest between them.

a = int(input("Enter first number :")) 
b = int(input("Enter another number :"))

if a > b:
    print("A is greater than B.")
elif a==b:
    print("Both are equal , it is an invalid case.")
else:
    print("B is greater than A.")