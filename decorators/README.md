# Decorators

Decorators are one of the metaprogramming concepts that deal with decorating a function without
modifying the actual function body. As the name suggests, a decorator adds additional value to a
function, a method, or a class by allowing the function to become an argument of another function
that decorates or gives more information on the function, method, or class being decorated. Decorators
can be developed on an individual user-defined function or on a method that is defined inside a class,
or they can be defined on a class itself too. Understanding decorators will help us to enhance the
reusability of functions, methods, and classes by manipulating them externally without impacting
the actual implementation.
We will be taking a look at the following main topics:
    • Looking into simple function decorators
    • Exchanging decorators from one function to another
    • Applying multiple decorators to one function
    • Exploring class decorators
    • Getting to know built-in decorator

## Exploring class decorators

A class decorator is similar to the function decorator that we discussed earlier. Class decorators can
be used to decorate, modify behavior, or debug a function, similar to a function decorator, which
adds behavior to a function without actually modifying the function itself. A class decorator can be
defined as a class by using two of its default or built-in methods: `__init__` and _`_call_`_. Any
variable initialized as part of the `__init__` function of a class while creating an object instance of
the class becomes a variable of the class itself. Similarly, the `__call__` function of a class returns
a function object. If we want to use a class as a decorator, we need to make use of the combination of
these two built-in methods.
