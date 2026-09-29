def add(nums):
    total = sum(nums)
    print("sum =", total, "\n")
    return total

def subtract(a, b=0):
    diff = a - b
    print("difference =", diff, "\n")
    return diff

def multiply(nums):
    product = 1
    for x in nums:
        product *= x
    print("product =", product, "\n")
    return product

def divide(a, b=1):
    if b == 0:
        print("not defined\n")
        return None
    quotient = a // b
    remainder = a % b
    exact_division = a / b
    print("quotient =", quotient)
    print("remainder =", remainder)
    print("exact division =", exact_division, "\n")
    return quotient, remainder, exact_division
