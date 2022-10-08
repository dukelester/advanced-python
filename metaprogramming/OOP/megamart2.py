'''  Megamart is a simulated large retail store that sells multiple products across
different cities and consists of multiple branches.
'''

from datetime import datetime
from itertools import product


class Branch:
    """ A class with set methods """
    def __init__(self):
        self.sales = None
        self.product = None
        self.branch = None

    def set_branch(self, **branch):
        """ Everything about a branch """
        return branch

    def set_products(self, **product):
        """ The details for the product """
        return product

    def set_sales(self, **sales):
        """ The sales details """
        return sales

    def calc_tax(self):
        """ Calculating the selling price will be done in the following two steps:
        1. Calculate the price before tax by adding the purchase price with the product between the
        purchase price and profit margin percentage.
        2. Calculate the selling price by adding the price before tax, with the product
        between price before tax and sales tax rate.
        """
        branch = self.branch
        product_ = self.product
        sales = self.sales
        price_before_tax = sales["purchase_price"] + (sales["purchase_price"]
                                                      * sales["profit_margin"]
                                                    )
        selling_price = price_before_tax + (price_before_tax *sales["tax_rate"])
        sales["selling_price"] = selling_price
        print(f"Purchased at {price_before_tax} before tax and sold at {selling_price}")
        return branch, product_,sales

nairobi_branch = Branch()
nairobi_branch.branch = nairobi_branch.set_branch(
    branch_id=2345, branch_name="Nairobi branch", branch_city="Nairobi",
    branch_street="Nairobi, Waiyaki way 2344", branch_postal_code=456789,
)
nairobi_branch.product = nairobi_branch.set_products(
    product_id=200098, product_name="Shoes", price=3000, seller="shoe shiner ltd")
nairobi_branch.sales = nairobi_branch.set_sales(
    sales_id="S23454", product_id=200098, payment_amount=30000, quantity=10,
    profit_margin=0.2, tax_rate=0.452, purchase_price=300,
    payments ={
        "mpesa": 3000, "wire transfer": 27000,
    })

print(nairobi_branch.branch, nairobi_branch.product,nairobi_branch.sales, sep="\n")
print(f"\n {nairobi_branch.calc_tax()} ")

# Inheritance
class NairobiBranch(Branch):
    """ A class inheriting from the main Class ==> Branch class
    It will have all the properties and methods of the Branch class
    as well as its own attributes and methods.
    """
    def __init__(self):
        super().__init__()
        self.intercity_branch = None

    def set_management(self, **intercity_branch):
        """ This is a simple method to handle the intercity management
        functions which are defined uniquely per a city branch.
        """
        return intercity_branch

    def calculate_nairobi_tax(self):
        """ A method to claculate the tax in the Nairobi city only.
        As the tax can be different in each city.
        """
        branch = self.branch
        intercity_branch = self.intercity_branch
        sales = self.sales
        product_ = self.product
        price_before_tax = sales["purchase_price"] + (sales["purchase_price"]
                                                      * sales["profit_margin"]
                                                    )
        total_tax_rate = sales["tax_rate"] + sales["local_tax_rate"]
        final_selling_price = price_before_tax + (price_before_tax * total_tax_rate)
        sales["final_selling_price"] = final_selling_price
        return branch, intercity_branch, product_, sales

juja_branch = NairobiBranch()
juja_branch.branch = juja_branch.set_branch(
    branch_id=67890, branch_name="Juja branch", branch_city="Kiambu",
    branch_street="2356, JKUAT, Entry Road", branch_postal_code=62000,
)
juja_branch.intercity_branch = juja_branch.set_management(
    regional_manager="Jason Muhgwe", phone_number="+2547567890", age=40,
    date=datetime.now(), sub_branch_id=4567890,
    branch_manager="Lester Dlester",
)

juja_branch.product = juja_branch.set_products(
    product_id=456789, product_name="Clothes",
    price=800, seller="Latifa Fashion LTD",
)
juja_branch.sales = juja_branch.set_sales(
    sales_id="S9876567", product_id=456789, payment_amount=8000, quantity=10,
    profit_margin=0.5, tax_rate=0.462, purchase_price=600,local_tax_rate=0.055,
)

print(f"\n Branch Details : {juja_branch.branch} \n ")
print(f" Management Details : {juja_branch.intercity_branch} \n ")
print(f"Product Details : {juja_branch.product} \n ")
print(f" Sales Details : {juja_branch.sales} \n ")
print(f"\n Finale Sales details : {juja_branch.calculate_nairobi_tax()} \n ")
print(f"Finale Sales details : {juja_branch.calc_tax()}")
