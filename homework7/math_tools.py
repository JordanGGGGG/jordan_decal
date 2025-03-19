def add(a, b):
    '''This function inputs two variables and outputs their sum.'''
    return a + b

def subtract(a, b):
    '''This function inputs two variables and outputs their difference.'''
    return a - b

def multiply(a, b):
    '''This function inputs two variables and outputs their product.'''
    return a * b

def divide(a, b):
    '''This function inputs two variables, outputs an error if the denominator is equal to zero or outputs their quotient.'''
    if b == 0:
        return "divide by zero error"
    else:
        return a / b
