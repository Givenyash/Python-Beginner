#Function without any aurguments/Parameters
#These are known as positional arguments.
def hello():
    print("This is a hello function.")

hello()



#with arguments and parameters
def greet(name):
    print(f"Hello, {name}!")
greet("Yash")




#with arguments/parameters 
def sum(a,b):  #Parameters
    print(f"The sum of your numbers is {a + b}")

sum(12,45)    #Arguments
sum(45,45)




#The thing you accept in the function() are the Parameters.
#The thing you provide to the parameters are the Arguments. 

#Parameters act like the variables inside the function paranthesis and Arguments are the values which is stored in the parameters and then further used by the function itself. We can call a function multiple times.