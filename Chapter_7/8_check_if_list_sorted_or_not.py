list = [12,13,14,15,16]

for i in range(len(list)-1):
    if list[i] < list[i+1]:
        continue
    else:
        print("Your list is not sorted")
        break
else:
    print("Your list is sorted")