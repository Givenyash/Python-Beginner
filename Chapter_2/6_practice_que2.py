# take a number as input , convert it to a float.
# and print both original and converted values with their data types.

# by single variable
number = input("Enter number : ")
print("The original number is : ",number ,type(number))

number = float(number)
print("The converted number is : ",number ,type(number))

print("\n")

# by double variable
nums = input("Enter a value :")
convertedValue =float(nums)
print("Original value :", nums , "Data type :", type(nums))
print("Converted value :", convertedValue,  "Data type :", type(convertedValue))