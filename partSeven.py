print("Command Line Caclulator")

operation = input("What operation? (+, -, *, /, ^, %): ")

while operation != "quit":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    match operation:
        case "+":
            print(f"{num1} + {num2} = {num1+num2}")
        case "-":
            print(f"{num1} - {num2} = {num1-num2}")
        case "*":
            print(f"{num1} * {num2} = {num1*num2}")
        case "/":
            if num2 == 0:
                print("DIVIDE BY ZERO ERROR AAAAAAAAAAA")
            else:
                print(f"{num1} / {num2} = {num1/num2}")
        case "^":
            print(f"{num1}^{num2} = {num1**num2}")
        case "%":
            print(f"{num1} % {num2} = {num1%num2}")
        case "quit":
            print("Quitting the application")
        case _:
            print("Not valid opperation :(")
    
    print("")
    operation = input("What operation? (+, -, *, /, ^, %): ")


print("Quitting the application")