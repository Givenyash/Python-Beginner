#check wheather a number is prime or not...

num = int(input("Insert a valid value :"))

count = 0
for i in range(2, num, 1):
    if num % i == 0:
        count = count + 1

if count == 0:
    print("Prime")

else:
    print("Not Prime")