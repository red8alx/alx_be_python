def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            result = num1 + num2
            return result
        case "subtract":
            result = num1 - num2
            return result
        case "multiply":
            result = num1 * num2
            return result
        case "divide":
            if num2 == 0:
                errorMsg = "Cannot divide by zero"
                return errorMsg
            elif num2 != 0:
                result = num1 / num2
                return result
        case _:
            print("Wrong type of operation")