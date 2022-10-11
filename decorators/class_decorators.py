""" A class decorator is similar to the function decorator that we discussed earlier.
Class decorators can be used to decorate, modify behavior, or debug a function,
similar to a function decorator, which adds behavior to a function without actually
modifying the function itself. A class decorator can be defined as a class by using
two of its default or built-in methods: `__init__` and _`_call_`_. Any variable initialized
as part of the `__init__` function of a class while creating an object instance of the class becomes
a variable of the class itself. Similarly, the `__call__` function of a class returns
a function object. If we want to use a class as a decorator, we need to make use of the
combination of these two built-in methods.
"""

class ClassDecorator:
    """ A simple class decorator """
    def __init__(self, input_function):
        self.input_function = input_function

    # def decorator(self):
    #     """ A decorator function """
    #     result = self.input_function()
    #     result_decorator = ' decorated by a class decorator'
    #     return result + result_decorator
    def __call__(self):
        """ A decorator function """
        result = self.input_function()
        result_decorator = ' decorated by a class decorator'
        return result + result_decorator

@ClassDecorator
def my_input_function():
    """ a function under a decorator """
    return 'This is input function'

print(my_input_function())
