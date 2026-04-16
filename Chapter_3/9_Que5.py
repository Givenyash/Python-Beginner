#Accept a year and check if it is a leap year or not.

year = int(input("Enter the Year :"))

if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
    print(year,"is a leap year.")

else:
    print(year,"is not a leap year.")