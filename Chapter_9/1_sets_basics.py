# Terminologies in Set

# 1)Mutable : Sets are mutable, means that you can change the values of set...

# 2)Duplicates : You cannot have any duplicate values in set that means very element will be unique...

# 3)Unordered : Sets are unordered and you cannot access them through index values...

# 4)Heterogenous : Set is semi-heterogenous it can store some data types like string, numbers, tuples but not everything...

#Syntax of set

s = {1,2,3,4,5}  #curley braces in sets
print(type(s))


#How set stores value in python ???


# Each value in a set is hashed using a hash function (hash() in Python)...

# The hash is used as an index to store the element in memory...

# Since hashing does not maintain order, hence sets are unordered...

# Mutable objects like lists and dictionaries are not allowed...

a = hash("Hello")
print(a)

c = hash((1,2,344))
print(c)

#Traversing in Set

# A set cannot be traversed using the index values cause it is unordered and has no index. So, many times it will give random values.

a = {1,8,9,2,3,4,5}

for i in a:
    print(i)


# Methods in Sets

# Now set methods are very powerful cause you don't have any indexing you cannot change the values but set is mutable so we use methods for this.

# For adding and removing the elements you can use methods as follows...

s = {1,2,3}

s.add(4)                    #Adds an element to the set
s.remove(2)                 #Removes 2 (Raises an error if not found)
s.discard(5)                #Removes 5 (No error if not found)
popped_element = s.pop()    #Removes a random element
s.clear()                   #Removes all elements


# Methods if there are 2 sets used ...

A = {1, 2, 3}
B = {3, 4, 5}

union_set = A.union(B)                      #{1, 2, 3, 4, 5}
intersection_set = A.intersection(B)        #{3}
difference_set = A.difference(B)            #{1, 2}
symmetric_diff = A.symmetric_difference(B)  #{1, 2, 4, 5}


print(A | B)  # Union
print(A & B)  # Intersection
print(A - B)  # Difference
print(A ^ B)  # Symmetric Difference

# Compound operations 

B = B - A   # B -= A
print(B)