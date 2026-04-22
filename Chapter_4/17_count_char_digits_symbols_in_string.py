#Count all letters, digits and special symbols from a given string...
# Given : s = "P@#yn26at^&i5ve"


s = input("Enter a valid string :")
#s = "P@#yn26at^&i5ve"

char = 0
digits = 0
special_symbols = 0

for i in s:
    if i.isdigit():
        digits += 1
    
    elif i.isalpha():
        char += 1
    
    else:
        special_symbols += 1


print(f"Your chars are {char}\nYour digits are {digits}\nYour special symbols are {special_symbols}")