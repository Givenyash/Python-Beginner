list = [12, 567, 43, 235, 347, 568, 45, 7]

largest = list[0]
index = 0

for i in range(len(list)):
    if list[i] > largest:
        largest = list[i]
        index = i

print(f"Your largest number is {largest} at index {index}")