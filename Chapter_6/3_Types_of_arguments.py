#There are 3 types of arguments that we can pass to parameters :- 
# 1)- Positional Argument
# 2)- Default Argument
# 3)- Keyword Argument

#Positional Argument

def sum(a,b):
    return a + b
print(sum(25,20))


#Keyword Argument

def hello(name,age):
    print(f"Your name is {name} and your age is {age}.")
# hello("Yash", 20)
hello(age = 20, name = "Yash")


#Default Argument

def sum(a,b=25):
    print(f"The sum is {a+b}")
# sum(20)    # a = 20 , b = 25
sum(20, 20)  # a = 20, b = 20

