#Take a number as input and print its table...

n = int(input("Enter a number :"))
for i in range(n , n*10+1 , 5):
    print(i)

#One more way to run loops
n = int(input("Enter a number: "))

for i in range(1, 11):   # i ki value 1 se 10 rahegi iss range me
    print(n, "x", i, "=", n * i)