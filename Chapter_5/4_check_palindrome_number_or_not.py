#Accept a number and check if it is a palindromeic number...

n = int(input("Enter a number :"))

num = n
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10 

if num == rev:
    print(f"{num} is Palindromic number")

else:
    print(f"{num} is not a palindromic number")
