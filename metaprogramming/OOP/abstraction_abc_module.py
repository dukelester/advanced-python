""" Abstraction is a concept of OOP that helps in hiding internal details of a class
or methods by providing a reference class with declarations of classes with
empty declarations of methods.
"""
from abc import ABC, abstractmethod

class Branch(ABC):
    """ A simple branch class to used as the Abstract Class
    inheriting from the ABC class for the abc.
    """

    @abstractmethod
    def maintanance_cost(self):
        """ Abstract method with the @abstractmethod decorator"""

class Nairobi(Branch):
    """ the Nairobi class, we will calculate the maintenance cost only if the
    product type is FMCG(Fast Moving Consumer Goods).
    """
    def __init__(self, product_type, quantity):
        self.product_type = product_type
        self.quantity = quantity

    def maintanance_cost(self, cold_storage=100):
        """ We will calculate the product of quantity costing 0.25 and add 100 USD for
        cold storage. If the product type is anything other than FMCG, we will notify
        you that the product will not be stocked.
        """
        if self.product_type == "FMCG":
            return (self.quantity * 0.25) + cold_storage
        return "We do not have the product in the stock"

class Mombasa(Branch):
    """ In the following code, for the Mombasa class, we will calculate maintenance cost
    only if the product type is Electronics. :
    """
    def __init__(self, product_type, quantity):
        self.product_type = product_type
        self.quantity = quantity

    def maintanance_cost(self):
        """ We will calculate the product of quantity costing 0.05 since the maintenance
        cost for electronics is lower and there is also no cold storage cost required here.
        If the product type is anything other than Electronics, we will notify that
        the product will not be stocked.
        """
        if self.product_type == "Electronics":
            return self.quantity * 0.05
        return "We do not have the product in the stock"

nairobi = Nairobi("FMCG", 2000)
mombasa = Mombasa("Electronics", 2000)

print(nairobi.maintanance_cost())
print(mombasa.maintanance_cost())
