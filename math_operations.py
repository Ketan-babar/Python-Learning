def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def sqrt(a):
    if a < 0:
        return "Cannot compute square root of negative number"
    return a ** 0.5

def factorial(n):
    if n < 0:
        return "Cannot compute factorial of negative number"
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result