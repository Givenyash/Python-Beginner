money = int(input("Please give me money :"))

if 0<=money<100: 
    print("I will have a choco bar ice-cream.") #True

elif 100<=money<=200:
    print("I can buy now more than 10 ice-creams.") #True agar first condition fail hui toh

else: 
    print("I can't handle handle the money. ") #False

# This is called as if-else ladder or nested if-else.
# elif checks conditions in sequence.