""" We will create two classes and add the buy_product method to each class to calculate the sales
price without adding a class decorator.
"""

class Kericho:
    """ A class for a Branch"""
    def __init__(self, product, unit_price, quantity, promotion_type):
        self.product = product
        self.unit_price = unit_price
        self.quantity = quantity
        self.promotion_type = promotion_type

    def  buy_product(self, kericho_tax_rate=0.0522):
        """ A method to handle the buying of a product """
        initial_price = self.unit_price * self.quantity
        total_tax = initial_price * kericho_tax_rate
        sales_price = initial_price + total_tax
        return sales_price, self.product, self.promotion_type

kericho = Kericho("Mobile phones", 20000, 20, "Discount")
print(kericho.buy_product())
