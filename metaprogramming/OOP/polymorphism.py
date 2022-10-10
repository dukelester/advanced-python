""" Implementing the Indepedent polymorphisim """

class Brooklyn:
    """ the Brooklyn class, we will calculate the maintenance cost only if the
    product type is FMCG(Fast Moving Consumer Goods)
    .
    """
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def cost_management(self, cold_storage=100):
        """ We will calculate the product of quantity costing 0.25 and add 100 USD for
        cold storage. If the product type is anything other than FMCG, we will notify
        you that the product will not be stocked.
        """
        if self.product == "FMCG":
            return (self.quantity * 0.25) + cold_storage
        return "We do not have such product in our branch"

class Queens:
    """ In the following code, for the Queens class, we will calculate maintenance cost
    only if the product type is Electronics. :
    """
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def cost_management(self):
        """ We will calculate the product of quantity costing 0.05 since the maintenance
        cost for electronics is lower and there is also no cold storage cost required here.
        If the product type is anything other than Electronics, we will notify that
        the product will not be stocked.
        """
        if self.product == "Electronics":
            return self.quantity * 0.05
        return "We do not have such product in our branch"

object_brooklyn = Brooklyn("FMCG", 200)
object_queens = Queens("Electronics", 900)

object_brooklyn = Brooklyn("FMCG", 2000)
object_queens = Queens("Electronics", 2000)

print(object_brooklyn.cost_management())
print(object_queens.cost_management())
