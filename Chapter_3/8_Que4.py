#Accept name and age from user. Check if the user is a valid voter or not.

name = input("Enter name :")
age = int(input("Enter your age :"))

if age >= 18:
    print("The voter", name,"is eligible for voting.")

else:
    print("The voter", name,"is not eligible for voting.")