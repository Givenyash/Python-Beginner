# Range function :  The range function is used to generate a sequence of numbers, which is commonly used in loops.

# Syntax of range function :- range(start, stop, steps). If you don't mention the steps the default steps will be 0 and the start point default as 0.

#You hve to mention the stop point , otherwise it will run infinately or the range function will not work.

#For loop
a = range(1,20,1) # prints 1 to 19

for i in a:
    print("Forward for loop",i)

#print 16 to 1

for i in range(16,0,-1):
    print("reverse for loop",i)

#Table of 5

for i in range(5,51,5):
    print("Table of 5", i)

#For printing any number of table

nums = int(input("Enter a number to print its table :"))

for i in range(nums, (nums*10)+1 , nums):
    print(f"Table of {nums} = {i}")