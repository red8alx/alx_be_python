number_1 = int(input("Enter the first number:"))
number_2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /): ")
match operation:
    case "+":
        result = number_1 + number_2
        print("The result is", result)
    case "-":
        result = number_1 - number_2
        print("The result is", result)
    case "*":
        result = number_1 * number_2
        print("The result is", result)
    case "/":
        if number_2 == 0:
            print("Cannot divide by zero")
        else:
            result = number_1 / number_2
            print("The result is", result)
    case _:
        print("Wrong type operation")
