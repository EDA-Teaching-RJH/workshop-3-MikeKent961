print("Purchase Movie Ticket:")
userAge = int(input("What is your age?: "))

if userAge < 12 or userAge >= 65:
    print("Your ticket is £5")
else:
    isUserStudent = input("Are you a student? (yes/no):  ")
    if isUserStudent == "yes":
        print("Your ticket is £8")
    else:
        print("Your ticket price is £10")
