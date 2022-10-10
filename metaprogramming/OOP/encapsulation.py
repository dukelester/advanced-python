""" we will define our familiar Branch class with private variables for product ID, product
name, brand, purchase price, and profit margin and create a private method to display the product
details. We will also create branch ID, regional manager, and branch manager as class variables that
are not private and look at the difference between accessing those using objects outside the class.
"""

class Branch:
    """Branch class with private variables for product ID, product
name, brand, purchase price, and profit margin and create a private method to display the product
details. """
    branch_id = 98745678
    reagonal_manager = "Duke lester"
    branch_manager = "John Kimbo"

    __product_id = 987655672
    __product_name = "Addidas Shoes Green"
    __purchase_price = 4000
    __product_brand = None
    __produc_profit_margin = None

    def __repr__(self):
        return f" Product Id : {self.__product_id} Product name : {self.__product_name}\
                Product Purchase Price : {self.__purchase_price} Product Brand : {self.__product_brand} \
                Product profit margin : {self.__produc_profit_margin}"

    def __display_product_details(self):
        """ Private method to display the product details """
        self.__product_id = 34567890
        self.__product_name = "Johnsons Soccer Boots"
        self.__purchase_price = 8000
        self.__product_brand = "The Johnsons"
        self.__produc_profit_margin = 0.67
        return f" Product Id : {self.__product_id} Product name : {self.__product_name} \
                Product Purchase Price : {self.__purchase_price} Product Brand : {self.__product_brand} \
                Product profit margin : {self.__produc_profit_margin}"
    def __init__(self):
        self.__display_product_details()
test_branch = Branch()
print(test_branch.branch_id)
# print(test_branch._Branch__display_product_details())


class BranchRecreated:
    """ Recreate the Branch class with protected variables for product ID, product
    name, brand, purchase price, and profit margin and create a protected method to display
    the product details. We will create a branch manager as a private variable.
    We will also create branch ID and regional manager as class variables that are
    not protected or private and look at the difference in accessing those using objects
    outside the class. We will also inherit the Branch class further to check which members are accessible.
"""
    branch_id = 98745678
    reagonal_manager = "Duke lester"
    branch_manager = "John Kimbo"

    _product_id = 987655672
    _product_name = "Addidas Shoes Green"
    _purchase_price = 4000
    _product_brand = None
    _produc_profit_margin = None
    __branch_manager_1 = "Lester dlester"

    def _display_product_details(self):
        """ Private method to display the product details """
        self._product_id = 34567890
        self._product_name = "Johnsons Soccer Boots"
        self._purchase_price = 8000
        self._product_brand = "The Johnsons"
        self._produc_profit_margin = 0.67
        return f" Product Id : {self._product_id} Product name : {self._product_name} \
                Product Purchase Price : {self._purchase_price} Product Brand : {self._product_brand} \
                Product profit margin : {self._produc_profit_margin}, Branch Manager{self.__branch_manager_1}"

    def __init__(self):
        self._display_product_details()
branch = BranchRecreated()
print(branch._display_product_details(), " ==>Protected member")

class Nairobi(BranchRecreated):
    """ inherits the parent class, Branch. The child class
will inherit all the protected variables and methods from the parent class,
whereas it will still not inherit the private members:
"""
    def __init__(self):
        super().__init__()
        print(self._product_id, "The protected ")
        print(self._display_product_details())

new_nairobi = Nairobi()
print(new_nairobi, new_nairobi.branch_manager)
print(new_nairobi.__branch_manager_1) # AttributeError
