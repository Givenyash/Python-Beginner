#Accept the gender from user as char and print the respective greeting message.

gender = input("What is your gender ?")

if gender == "male" or 'Male' or 'MALE':
    print("Hello!! this message is for male candidates.")

elif gender == "female"or 'Female' or 'FEMALE':
    print("Hey!! this message is for female candidates.")

else:
    print("hola!! this message is for other category.")
    print("Are you Gay or Lesbian ??")