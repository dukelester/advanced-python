""" If we want different functions to show specific additional information,
no matter what the functions perform, We can do this simply by defining
another function that decorates any function that is provided as an input.
"""

def function_decorator(input_function):
    """ A simple function """
    def decorator():
        """ A simple decorator function to print an extra line"""
        print("--- Decorate function with this line ---")
        return input_function()
    return decorator

# Create new functions to be used as decorators
# Syntax 0ne
def user_function_one():
    """ A simple function to print a phrase """
    return "A picture is worth a thousand words "

def user_function_two():
    """ A simple function to print a phrase """
    return "Actions speak louder than words"

decorated_function_one = function_decorator(user_function_one)
decorated_function_two = function_decorator(user_function_two)
print("decorator 1 ==>", decorated_function_one())
print("decorator 2 ==>", decorated_function_two())

print("\n ****************** Second syntax **************** \n")
# Method 2

@function_decorator
def user_decorated_function():
    """ Decorated function """
    return "I am a decorated function here and now "

@function_decorator
def user_decorated_function_two():
    """ Decorated function """
    return "I am a second decorated function here and now "

print(user_decorated_function())
print(user_decorated_function_two())
