list = [23, 43, 555, 532, 56, 21]

largest = list[0]
secondLargest = list[0]

for i in range(len(list)):
    if list[i] > largest:
        secondLargest = largest
        largest = list[i]
    
    elif list[i] > secondLargest:
        secondLargest = list[i]
      
print(f"Your second largest number is {secondLargest}")
 