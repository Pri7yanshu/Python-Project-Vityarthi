# Extras module: exponential and factorial
 
def exponential(a, b):
    if a == 0 and b < 0:
        print("0 cannot be raised to a negative power\n")
        return None
    if a < 0 and b != int(b):
        print("negative number with a fractional power is not defined\n")
        return None
    power = a ** b
    print(a, "raised to the power", b, "=", power, "\n")
    return power
 
 
def factorial(n):
    if n < 0:
        print("factorial not defined for negative numbers\n")
        return None
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("factorial(", n, ") =", fact, "\n")
    return fact