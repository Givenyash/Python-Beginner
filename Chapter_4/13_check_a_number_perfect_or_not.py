#Accept a number and check if it a perfect number or not...
#Perfect number :- a number whose sum of factors is equal to the number itself...

num = int(input("Insert a number you want to check :"))

sum = 0
for i in range(1, num+1 , 1):
    if num % i == 0:
        sum = sum + i

if sum == num:
    print(f"The given number {num} is a perfect number")

else:
    print(f"The given number {num} is not a perfect number")