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
    branch_mamnager = "John Kimbo"

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
