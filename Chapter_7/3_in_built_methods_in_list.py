#Some of the examples of the methods in the List...
numbers = [5, 2, 9, 1, 5, 6]

numbers.append(10)                  #Adds 10 to the end
numbers.insert(2,15)                #Insert 15 at index 2
numbers.extend([20, 25, 30])        #Adds multiple elements at the end
numbers.remove(5)                   #Remove the first occurance of 5
popped_item = numbers.pop(3)        #Removes and stores the element at index 3
index = numbers.index(6)            #Finds the index of 6
countNum = numbers.count(5)         #Counts occurance of 5
numbers.sort()                      #Sorts the list in ascending order
numbers.reverse()                   #Rverses the list order
new_numbers = numbers.copy()        #Creates a copy of the list
numbers.clear()                     #removes all elements from the list
del numbers[5]                      #Deletes an element at a specific index


#Nested list is used to print a Matrix which is 2D