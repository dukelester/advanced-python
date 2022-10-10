""" Python also supports multiple inheritance, where we can import a
subclass from more than one base class or parent class.
In such a scenario, the child class or the subclass inherits all the attributes and
methods of the base classes. In this example, we will create two base classes,
Product and Branch, and let the Sales class inherit both these base classes
"""

from datetime import datetime


class Product:
    """ We will be creating a Product class where we will define the attributes for a
    product and a get_product method to return the product details
    """
    _product_id = 567890
    _product_name = "Iphone X Max"
    _product_seller = "Lester Electronics"
    _product_category = "Electronics"
    _unit_price = 7000

    def get_product(self):
        """ A method for product details """
        return (self._product_id, self._product_name, self._product_category,
                self._product_seller, self._unit_price,
                )


class Branch:
    """ Creating another class, Branch, where we will define the attributes
    for a branch and a get_branch method to return the branch details:
    """
    _branch_id = 67890003
    _branch_name = "Nairobi Branch"
    _branch_city = "Nairobi Kenya"
    _branch_zip = 34003
    _branch_street = '234, Uhuru Way'

    def get_branch(self):
        """ A method to display the branch information """
        return (self._branch_id, self._branch_name, self._branch_city,
                self._branch_street, self._branch_zip,
                )

# Implementig multiple inheritence
class Sales(Product, Branch):
    """ We will be implementing the concept of multiple inheritance by inheriting
    two parent classes, Product and Branch, into the child class, Sales
    """
    date = datetime.utcnow()

    def get_sales(self):
        """ To get the sales details """
        return (self.date, Product.get_product(self), Branch.get_branch(self))

# Creating the object
sales = Sales()
print(sales.get_branch())
print(sales.get_product())
print(sales.get_sales())
