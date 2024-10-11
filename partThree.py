grade = int(input("What was the grade? "))

while grade >100 or grade < 0:
    grade = int(input("Invalid input. Try again: "))

if grade <= 100 and grade >= 90:
    print("You got an 'A', wow you are the best :D")
elif grade < 90 and grade >=80:
    print("You got a 'B', pretty good :)")
elif grade <80 and grade >=70:
    print("You got a 'C', that's an ok grade :>")
elif grade <70 and grade >=60:
    print("You got a 'D', you should definitely improve :(")
else:
    print("You got an 'F', YOU FAILED D:")     
