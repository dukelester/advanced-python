""" Introduction to python metaprogramming """

import operator as op

def addition(arg1, arg2):
    """ A simple function which takes two arguments and computes their sum"""

    return arg1 + arg2

print(addition(89, 80))
print(addition("hello", "duke lester"))
# print(addition(34, "hello duke lester")) ==> Rreturns an error

# ''' TODO: Error TypeError: unsupported operand type(s) for +: 'int' and 'str'
# using the Metaprogramming
# '''

def addinition_solved(var1, var2):
    """ Solving the Type error using the metaprogramming """
    if (isinstance(var1, str) and isinstance(var2, int)
		or isinstance(var1, int) and isinstance(var2, str)
		):
        return "Please enter both input values as integers or string \n"
    result = var1 + var2
    return result

print(addinition_solved(89, 80))
print(addinition_solved("hello", "duke lester"))
print(addinition_solved(34, "hello duke lester"))
print(addinition_solved("duke lester doing metaprogramming", 45))

def subtract(a, b):
    """ A simple function to subtract two operands """
    return a - b

print(subtract(34, 9))
print(subtract(34, 90))
# print(subtract("hello", "test")) ==> Error --> Type error

def subtract_solved(a, b):
    """ Using the metaprogramming to solve the error of
	TypeError: unsupported operand type(s) for -: 'str' and 'str'
	"""
    if (isinstance(a, str) and isinstance(b, str) or
		isinstance(a, str) and isinstance(b, int) or
		isinstance(a, int) and isinstance(b, str)
		):
        print("Cannot subtract strings. Please enter numbers only!")
    return a - b

print(subtract_solved(34, 9))
print(subtract_solved(34, 90))
print(subtract_solved("hello", "test"))
print(subtract_solved(90, "testing a subtraction"))
print(subtract_solved("Number 34", 98))

def addition_of_numbers(num_1, num_2):
    """ Addition of only numbers """

    if (isinstance(num_1, int) and isinstance(num_2, int) or
		isinstance(num_1, float) and isinstance(num_2, float) or
		isinstance(num_1, float) and isinstance(num_2, int) or
		isinstance(num_1, int) and isinstance(num_2, float)
		):
        return num_1 + num_2
    return "Please enter numbers only to cumpute the sum"

print(addition_of_numbers(34, 89))
print(addition_of_numbers(34.00778, 89))
print(addition_of_numbers(34, 89.7622))
print(addition_of_numbers(34.522, 89.7892))
print(addition_of_numbers(34, "Number 2"))
print(addition_of_numbers("hello duke lester", 89))
print(addition_of_numbers('34', '89'))

# The DRY Principal

def arithmetic(num1, num2, operation):
    """ This is a simple function to carry put basic arithmetic
	functions and operations on two numbers.
	"""
    return operation(num1, num2)

print(arithmetic(23, 44, op.add))
print(arithmetic(23, 44, op.sub))
print(arithmetic(23, 44, op.mul))
print(arithmetic(40, 78, op.truediv))
