"""
we will create a function to add an email signature for a branch manager in a
different format for each branch. We will define two functions, manager_nairobi
and manager_mombasa, with different font colors and highlights.
"""

def signature(branch):
    """ let us add the name of ABC Megamart in both the signatures with a yellow highlight and
    modify the font color of the signature to yellow while keeping the signature highlight colors
    intact. To do this,
    """
    def footnote(*args):
        """we will create a function decorator that takes in the arguments of
        the preceding functions and add ABC Megamart with a black font and yellow highlight.
        """
        LOGO = '\33[43m'
        print(f"{LOGO} ABC Mega Mart")
        print(*{
            "postal Code": 567," contact email": "contactus@gmail.com"
        }.values())
        return branch(*args)
    return footnote


def product_discount_decorator(product):
    """ A simple product decorator """
    def product_decorator(**product_details):
        print("The product details here ... and the discount..")
        return product(**product_details)
    return product_decorator

@signature
def manager_nairobi(*args):
    """ A simple function decorator """
    BLUE = '\033[94m'
    BOLD = '\33[5m'
    SELECT = '\33[7m'
    for arg in args:
        print(BLUE + BOLD + SELECT + str(arg))

print(manager_nairobi("Duke lester",34,"Nairobi","lester5@gmail.com"))

print("\n**********************************************\n")

@signature
def manager_mombasa(*args):
    """ A simple function decorator for mombasa """
    GREEN = '\033[92m'
    SELECT = '\33[7m'
    for arg in args:
        print(SELECT + GREEN + str(arg))

print(manager_mombasa("Jacob Mwanu",34,"Mombasa","jacob5@gmail.com"))

@product_discount_decorator
def product_details_function(**product_details):
    """ Get the product details """
    return product_details
print(product_details_function(product_name="Addidas Shoes",price=2300, shop_number=3))
