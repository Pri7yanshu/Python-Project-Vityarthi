# Scientific module: trigonometry, logarithm, roots
import numpy as np


def sine(x):
    result = np.sin(np.radians(x))      # x is in degrees
    print("sin(", x, ") =", result, "\n")
    return result


def cosine(x):
    result = np.cos(np.radians(x))
    print("cos(", x, ") =", result, "\n")
    return result


def tangent(x):
    # tan is not defined at 90, 270, ... degrees
    if x % 180 == 90:
        print("tan is not defined for", x, "degrees\n")
        return None
    result = np.tan(np.radians(x))
    print("tan(", x, ") =", result, "\n")
    return result


def logarithm(x):
    if x <= 0:
        print("logarithm not defined for non-positive numbers\n")
        return None
    log10 = np.log10(x)
    ln = np.log(x)
    log2 = np.log2(x)
    print("log10(", x, ") =", log10)
    print("ln(", x, ") =", ln)
    print("log2(", x, ") =", log2, "\n")
    return log10, ln, log2


def square_root(x):
    if x < 0:
        print("square root not defined for negative numbers\n")
        return None
    result = np.sqrt(x)
    print("square root of", x, "=", result, "\n")
    return result


def cube_root(x):
    result = np.cbrt(x)
    print("cube root of", x, "=", result, "\n")
    return result