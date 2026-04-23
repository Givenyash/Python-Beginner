#Terminology in List

# 1) Mutable- Mutability referes to wheather an object's value can be changed after creation. And List allows this.  

# 2) Duplicates- We know data structures are used to store multiple values so duplicates means same value occuring multiple time. List allows this.

#3) Ordered- List maintains ordered data structure, maintains the sequence of elements as they were inserted. This means you can access elements using their position (index).

# 4) Heterogenous- List have heterogenous nature that means we can have multiple data types inside the list.


#Syntax of List : declared using square brackets...

fruits = ["Apple", "Banana", "Cherry"]
num = [12, 13, 14, 15, 10, 75.85, True, print()]
print(num[0:6])           #This is called slicing in List

#Mutable List --> Arrays in c++
numbers = [10,20,30]
numbers[1] = 99
print(numbers)            #output: [10,99,30]


#Traversing in List

#1st way
for i in range(len(numbers)):
    print(numbers[i])

#2nd way      here you can't access the indeces.
for i in numbers:
    print(i)