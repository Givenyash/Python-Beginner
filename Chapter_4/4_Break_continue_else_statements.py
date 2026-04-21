#Break ends the current loop based on the condition...
#Continue skips the number of iterations based on the condition...

#break
for i in range(1,21):
    if i == 15:       #print 1 to 14 (output)
        break
    else:
        print(i)


#continue
for i in range(1,21):
    if i == 15:       #print 1 to 14 (output)
        continue
    print(i)


#else :- It works with break, if break does not runs then else statement will run...
for i in range(1,21):
    if i == 15:
        print("Break statement is executed")
        break
    print(i)

else:
    print("Break statement is not executed")

#else
for i in range(1,21):
    if i == 58:
        print("Break statement is executed")
        break
    print(i)

else:
    print("Break statement is not executed")