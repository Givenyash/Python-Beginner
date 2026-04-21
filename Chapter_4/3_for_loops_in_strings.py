#LOOPs for strings work slightly differently. We can iterate a string in two ways : 
# a.Using index values  b.Iterating directly over the string.

#If Iterating using the index values, we again have to use range function 
#Example :


#Index Value
s = "FUTURE "
for i in range(0,6,1):
    print(s[i])

#Indexing also includes spaces here , and counting starts from 1 not 0
str = "FUTURE OF AI IS VERY BRIGHT IN OUR LIFE" 
print(len(str)) #size of string (including spaces)
for i in range(len(str)):
   print(str[i])



#Directly iterate over a string
a = "SHERIANS IS COOL"
for i in a :
    print(i)