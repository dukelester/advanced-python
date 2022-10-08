'''  Megamart is a simulated large retail store that sells multiple products across
different cities and consists of multiple branches.
'''

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
