
# OOP (Object Oriented Programming)

But before we deep dive into the concepts of metaprogramming,
it is important for you to have knowledge of the basic Object-Oriented
Programming (OOP) concepts available in Python. This chapter gives an overview of the existing
OOP concepts along with examples.

## The main topics we will be covering in this chapter are as follows

    • Introducing our core example
    • Creating classes
    • Understanding objects
    • Applying methods
    • Implementing inheritance
    • Extending to multiple inheritance
    • Understanding polymorphism
    • Hiding details with abstraction
    • Protecting information with encapsulation

We will be making use of a simulated schema named `ABC Megamart` to explain
the concepts of OOP. The availability of an object-oriented approach in a programming language helps with effective reusability and abstraction of the language. Our example, `ABC Megamart`, is a simulated
large retail store that sells multiple products across different cities and consists of multiple branches.
Let us give a structure to different entities of this store and look at how they can fit into an organized OOP paradigm.

## Our store consists of the following

    • Products
    • Branches
    • Invoices
    • Holidays
    • Shelves
    • Inventory
    • Sales
    • Promotions/offers
    • Exchange counter
    • Finance
Each of these entities can have multiple attributes of data or information that are required to perform multiple functions in the smooth and efficient management of the stores.

Let us explore how these entities and their attributes can be structured into a software model developed
by applying the concepts of OOP:

    • Each of the preceding 10 entities can be connected either directly or indirectly
    • Each branch will have sales and each sale will have invoices
    • Each branch city will have holidays and sales can happen during holiday seasons
    • Each branch (store) can have shelves and products will be placed on shelves
    • Each product can have promotions or offers and promotions influence sales.

Let us look at what a class can look like. We can consider the Branch entity of ABC Megamart. A
Branch can have an ID and an Address. Address can further be detailed into Street, City,
State, and Zip code. If we consider Branch as a class, ID, Street, City, State, and Zip
code would become its attributes. All operations that can be performed by a branch will become
its methods.
A branch can sell products, maintain invoices, maintain inventory, and so on.

### A class can be defined as follows

class ClassName:
'''attributes...'''
'''methods...'''

class Branch:
'''attributes...'''
'''methods...'''

## Object

An `object` can be defined as the instance of the class. If we consider a class itself as a data type,
then an object can be defined as the variable of a class of type ClassName.

obj_name = ClassName()

## Applying methods

Methods are similar to the user-defined functions we create to perform various operations in a
program, the difference being methods are defined inside a class and are governed by the rules of the
class. Methods can be utilized only by calling them using an object instance created for that class.
User-defined functions, on the other hand, are global and can be called freely anywhere within the
program. A method can be as simple as printing a statement or can be a highly complex mathematical
calculation that involves a large number of parameters.

## Implementing inheritance

Inheritance in a literal sense means acquiring the properties of a parent by the child, and it means
the same in the case of OOP too. A new class can inherit the attributes and methods of a parent class
and it can also have its own properties and methods. The new class that inherits the parent class will
be called a child class or a subclass while the parent class can also be called a base class.

The general structure of inheritance while defining a child class inheriting from a parent class looks
as follows:
    class Parent:
    '''attributes...'''
    '''methods...'''
    class Child(Parent):
    '''attributes...'''
    '''methods...'''

# Extending to multiple inheritance

Python also supports multiple inheritance, where we can import a subclass from more than one base
class or parent class. In such a scenario, the child class or the subclass inherits all the attributes and
methods of the base classes. In this example, we will create two base classes, Product and Branch,
and let the Sales class inherit both these base classes.

We will be implementing the concept of multiple inheritance by inheriting two parent classes, Product
and Branch, into the child class, Sales.

## Understanding polymorphism

Polymorphism is the concept of the OOP paradigm where we can reuse the name of a function from
a parent class either by redefining or overriding an existing function or by creating two different
functions for two different classes with the same name and using them separately.

    • Polymorphism within inheritance
    • Polymorphism in independent classes
