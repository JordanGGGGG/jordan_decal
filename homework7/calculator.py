import math_tools as mt

a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))

c = str(input("Which operation would you like to perform?:"))

#print(c) Testing c variable
#print(a + b) Testing if a and b return the numbers you input

def Calc_short_for_calculator(a, b, c):
    if c == "add":
        result = mt.add(a, b)
    elif c == "subtract":
        result = mt.subtract(a, b)
    elif c == "multiply":
        result = mt.multiply(a, b)
    elif c == "divide":
        result = mt.divide(a, b)
    else:
        return "Invalid Operation"
    return result

print(Calc_short_for_calculator(a, b, c))