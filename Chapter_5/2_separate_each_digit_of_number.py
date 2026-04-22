#Separate each digit of a number and print it on the new line.

n = int(input("Enter a number :"))

while n > 0:
    k = n % 10
    print(k)
    n = n // 10 