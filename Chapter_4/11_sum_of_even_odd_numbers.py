#print the sum of even and odd numbers in range separately...

num = int(input("Enter a number :"))

evenSum = 0
oddSum = 0

for i in range(0, num + 1):
    if i % 2 != 0:
        oddSum = oddSum + i
    
    else:
        evenSum += i

print(f"The sum of even and odd numbers upto {num} is => even Sum = {evenSum} , odd Sum = {oddSum}")