
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
