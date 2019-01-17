def Plus(firstNumber, secondNumber):
    result = firstNumber + secondNumber
    return result


def Minus(firstNumber, secondNumber):
    result = firstNumber - secondNumber
    return result


def Share(firstNumber, secondNumber):
    result = firstNumber / secondNumber
    return result


def multiplication(firstNumber, secondNumber):
    result = firstNumber * secondNumber
    return result

while True:

    result = 0

    firstNumber = int(input("Первое число"))
    sign = input("Знак")
    secondNumber = int(input("Второе число"))

    if sign == "+":
        print(Plus(firstNumber, secondNumber))
    elif sign == "-":
        print(Minus(firstNumber, secondNumber))
    elif sign == "/":
        print(Share(firstNumber, secondNumber))
    elif sign == "*":
        print(multiplication(firstNumber, secondNumber))
    else:
        print("Error")




