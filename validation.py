# Validation module: keeps asking until the user types a valid value
# so that the program does not crash on wrong input.

def get_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_float(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_count(message):
    # how many numbers to add/multiply, must be at least 1
    while True:
        count = get_int(message)
        if count >= 1:
            return count
        print("Please enter 1 or more.")
