"""
A small CLI application that endlessly takes user input and evaluates it as a mathematical expression
"""
from math_evaluator import calc

while True:
    # this will raise a SyntaxError if the expression is syntactically incorrect
    # normally you should always catch that Exception
    expression = input(">>> ")
    print(calc(expression))