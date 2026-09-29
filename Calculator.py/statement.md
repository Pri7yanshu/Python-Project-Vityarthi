# Project Statement

## Problem Statement
Students often need to switch between basic arithmetic and scientific calculations such as trigonometry, logarithms, roots, powers and factorials. A physical calculator is not always available, and many software calculators crash or give confusing output when the user enters something wrong. There is a need for a simple calculator that runs anywhere Python is installed, shows clear results and handles mistakes safely.

## Scope of the Project
**In scope**
- A menu-driven command-line calculator written in Python.
- Basic arithmetic: add and multiply any number of values, subtract, and divide (quotient, remainder and exact result).
- Scientific functions: sine, cosine, tangent (in degrees), logarithms (log10, ln, log2), square root and cube root.
- Extra operations: exponential (power) and factorial.
- Code divided into modules: Arithmetic, scientific, extras, validation and the main program.
- Input validation and error handling for wrong menu choices, non-numeric input, division by zero, log of non-positive numbers, square root of negative numbers, tan(90) and negative factorial.
- A history of calculations made in the current session.
- Simple unit tests for all operations.

**Out of scope**
- Graphical or web interface.
- Graph plotting, symbolic algebra and complex numbers.
- Saving history permanently to a file or database (future enhancement).

## Target Users
- School and college students who need quick arithmetic and scientific calculations.
- Beginners learning Python who want an example of a modular, menu-driven program.

## High-Level Features
- Numbered menu with 12 operations, a history option and an exit option.
- Add or multiply as many numbers as the user wants.
- Division shows quotient, remainder and exact value together.
- Trigonometric functions take angles in degrees.
- Logarithms, square root, cube root, power and factorial.
- Wrong input is rejected with a message and the user is asked again.
- Undefined operations show a clear message instead of crashing.
- Session history and a set of unit tests.

