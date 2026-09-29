# Main program: shows the menu and calls functions from the other modules
from Arithmetic import add, subtract, multiply, divide
from scientific import sine, cosine, tangent, logarithm, square_root, cube_root
from extras import exponential, factorial
from validation import get_int, get_float, get_count

functions = [
    "add", "subtract", "multiply", "divide",
    "sine", "cosine", "tangent", "logarithm",
    "square_root", "cube_root", "exponential", "factorial"
]

history = []   # stores the results of this session

while True:
    print("functions offered:", functions)
    print(
        "to add : i=0\n"
        "to subtract: i=1\n"
        "to multiply : i=2\n"
        "to divide : i=3\n"
        "for sine : i=4\n"
        "for cosine : i=5\n"
        "for tangent : i=6\n"
        "for logarithm : i=7\n"
        "for square root : i=8\n"
        "for cube root : i=9\n"
        "for exponential : i=10\n"
        "for factorial : i=11\n"
        "to see history : i=12\n"
        "to exit calculator : i=13"
    )

    i = get_int("enter value of function you want to perform: ")

    if i == 13:
        print("exiting calculator. GoodBye!\n")
        break

    elif i == 12:
        if len(history) == 0:
            print("no calculations yet\n")
        else:
            print("--- history ---")
            for item in history:
                print(item)
            print()

    elif i == 0:
        count = get_count("How many numbers do you want to add? ")
        nums = [get_float(f"Enter number {j+1}: ") for j in range(count)]
        result = add(nums)
        history.append(f"add {nums} = {result}")

    elif i == 1:
        a = get_float("enter first number: ")
        b = get_float("enter second number: ")
        result = subtract(a, b)
        history.append(f"subtract {a} - {b} = {result}")

    elif i == 2:
        count = get_count("How many numbers do you want to multiply? ")
        nums = [get_float(f"Enter number {j+1}: ") for j in range(count)]
        result = multiply(nums)
        history.append(f"multiply {nums} = {result}")

    elif i == 3:
        a = get_float("enter numerator: ")
        b = get_float("enter denominator: ")
        result = divide(a, b)
        history.append(f"divide {a} / {b} = {result}")

    elif i == 4:
        x = get_float("enter angle in degrees: ")
        result = sine(x)
        history.append(f"sin({x}) = {result}")

    elif i == 5:
        x = get_float("enter angle in degrees: ")
        result = cosine(x)
        history.append(f"cos({x}) = {result}")

    elif i == 6:
        x = get_float("enter angle in degrees: ")
        result = tangent(x)
        history.append(f"tan({x}) = {result}")

    elif i == 7:
        x = get_float("enter number: ")
        result = logarithm(x)
        history.append(f"logarithm({x}) = {result}")

    elif i == 8:
        x = get_float("enter number: ")
        result = square_root(x)
        history.append(f"square root({x}) = {result}")

    elif i == 9:
        x = get_float("enter number: ")
        result = cube_root(x)
        history.append(f"cube root({x}) = {result}")

    elif i == 10:
        a = get_float("enter base number: ")
        b = get_float("enter power: ")
        result = exponential(a, b)
        history.append(f"{a} ^ {b} = {result}")

    elif i == 11:
        n = get_int("enter number for factorial: ")
        result = factorial(n)
        history.append(f"factorial({n}) = {result}")

    else:
        print("invalid choice\n")