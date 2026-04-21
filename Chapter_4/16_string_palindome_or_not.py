#Check wheather a string is palindrome or not...

text = input("Enter your string to be check :")
s = ""

for i in range( len(text) - 1, 0-1, -1):
    s = s + text[i]

if s == text:
    print("Your string is a Palindrome string.")

else:
    print("Your string is not a Palindrome string.")