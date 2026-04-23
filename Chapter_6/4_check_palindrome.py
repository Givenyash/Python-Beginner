def palindrome(s):
    rev =""
    for i in range( len(s)-1, -1, -1):
        rev = rev + s[i]

    if rev == s:
        print(f"{s} Palindrome")
    else:
        print(f"{s} Not a Palindrome")

palindrome("Yash")
palindrome("naman")
