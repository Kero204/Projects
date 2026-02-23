""" operator = input("Enter an opretator (+ - * /): ")
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is not a valid operator")


 """

def addition(a, b):
    return a + b

def substraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero!"
    
import random

def random_operation():
    dice = random.randint(1, 7)
    if dice == 1:
        return "Addition"
    elif dice == 2:
        return "Substraction"
    elif dice == 3:
        return "Multiplication"
    elif dice == 4:
        return "Division"
    else:
        return "No operation"

addition = lambda a, b: a+ b


    


