import Calculator
import random

addition = Calculator.addition(5, 3)
print(f"addition: {addition}")

substraction = Calculator.substraction(5, 3)
print(f"substraction: {substraction}")

multiplication = Calculator.multiplication(5, 3)
print(f"multiplication: {multiplication}")

division = Calculator.division(5, 3)
print(f"Division: {division}")

calc = Calculator.random_operation()
print(f"Random operation: {calc}")