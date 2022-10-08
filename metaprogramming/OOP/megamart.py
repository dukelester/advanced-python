'''  Megamart is a simulated large retail store that sells multiple products across
different cities and consists of multiple branches.
'''

class SimpleBranch:
    """ Attributes """
    branch_id = None
    branch_street = None
    branch_city = None
    branch_state = None
    branch_zip = None

    # Methods
    def get_product(self):
        """ The method to handle products """
        return "product"

    def get_sales(self):
        """ The method to handle the sales """
        return "Sales"

    def get_invoice(self):
        """ THe method to handle the invoices """
        return "Invoices"

# Create an Object
branch_albany = SimpleBranch()
branch_albany.branch_id = 45678
branch_albany.branch_city = "Albama"
branch_albany.branch_street = "3456 St. Paulo Markos"
branch_albany.branch_state = "United States"
branch_albany.branch_zip = 56789
print(branch_albany.branch_zip, branch_albany.branch_city,branch_albany.branch_id,
    branch_albany.branch_state, branch_albany.branch_street, sep=" \n"
    )
branch_nevada = SimpleBranch()
branch_nevada.branch_id = 6678
print(branch_nevada.branch_id)

# New class with the init method

class Branch:
    """ A class using the constructor init """
    def __init__(self, branch_id, branch_name, branch_city,branch_street,
                branch_state,branch_zip):
        self.branch_name = branch_name
        self.branch_id = branch_id
        self.branch_street = branch_street
        self.branch_city = branch_city
        self.branch_state = branch_state
        self.branch_zip = branch_zip

    def __repr__(self) -> str:
        return f"Welcome to {self.branch_name.title()}"

        # Methods
    def get_product(self):
        """ The method to handle products """
        return "product"

    def get_sales(self):
        """ The method to handle the sales """
        return "Sales"

    def get_invoice(self):
        """ The method to handle the invoices """
        return "Invoices"

kenyan_branch = Branch(567893, "Kenyan Branch", "Nairobi", "Wahiyaki Way",
                    "Nairobi",8765567,
                    )
albany_branch = Branch(101,'Albama Branch','123 Main Street','Albany',
                    'New York', 12084,
                    )
print(kenyan_branch, albany_branch)
# Calling the class methods.
print(kenyan_branch.get_invoice())
print(kenyan_branch.get_product())
print(kenyan_branch.get_sales())
