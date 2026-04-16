#Create if elif ladder using multiple conditions of elif.

temp = int(input("Enter temperature :-"))

if temp < 0:
    print("Freezing cold")

elif temp >= 0 and temp < 10:
    print("very cold")

elif temp >= 10 and temp < 20:
    print("cold")

elif temp >= 20 and temp < 30:
    print("pleasant")

elif temp >= 30 and temp < 40:
    print("hot")

else:
    print("Temperature is very hot")