#There are only 2 methods in Tuple/

a = (1,2,3,4,5,5,5.5)

index = a.index(5)    #first occurance of 5
print(index)

count = a.count(5)
print(count)

# Tuple unpacking...

a,b,c,d = (1,2,3,4)
print(a,b,c,d)

a = (1)  #Acts as int because of tuple unpacking...
print(type(a))

a = (1,) #Acts as tuple because of comma after 1...
print(type(a))