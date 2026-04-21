#Print all the factors of a number

n = int(input("Insert a value :"))

for i in range(1 , n+1 , 1):
    if n % i == 0:
        print(f"The factors of a given number {n} are : {i}")