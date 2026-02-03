from decimal import DivisionByZero


def add(a, b): return a + b
def subtract(a, b): return a - b

def multiply(a,b):
    """Multiply two numbers."""
    return a * b

def divide(a,b): 
    if b == 0:
        raise DivisionByZero
    return a / b