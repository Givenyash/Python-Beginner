#Print positive and negative elements of a list...
l = [-45, 67, 12, -68, -69, 34]

print("Positive elements are ")
for i in l:
    if i >= 0:
        print(i)

print("Negative elements are ")
for i in l:
    if i < 0:
        print(i)