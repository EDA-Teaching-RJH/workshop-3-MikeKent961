import random

secretNumber = random.randint(1,10)
guess = int(input("Guess my number (between 1 and 10 inclusive): "))

while guess != secretNumber:
    if guess > 10 or guess < 1:
        guess = int(input("That's not between 1 and 10 (inclusive) silly. DO IT AGAIN: "))
    elif guess > secretNumber:
        guess = int(input("Your guess is too high, try again: "))
    else:
        guess = int(input("Your guess is too low, try again: "))

print("You got it, it was" , secretNumber , "yayy :D ")
    
