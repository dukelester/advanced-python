"""creating two different decorators to serve two different purposes and later utilizing them
by interchanging the decorators between different functions."""

from datetime import datetime

def date_converter(function):
    """ A date converter function
    date_converter is a decorator function that takes in another function as an
    argument.
    """
    def date_decorator(*args):
        """ The date decorator function"""
        arguments = []
        for arg in args:
            if isinstance(arg, datetime):
                arg = arg.weekday, arg.month, arg.day, arg.year
                arguments.append(arg)
        return function(*args)
    return date_decorator

@date_converter
def set_holiday_nairobi(*args):
    """ Takes in the arguments using
    the *args parameter. The first argument of this function will be set as branch_id, the second
    argument as holiday_type, the third argument as holiday_name, and the fourth argument
    as holiday_date. All of these input arguments are converted into a dictionary variable by the
    function and it returns the dictionary with its key-value pairs denoting each value.
    """
    holiday_details = {}
    holiday_details["branch_id"] = args[0]
    holiday_details["holiday_type"] = args[1]
    holiday_details["holiday_name"] = args[2]
    holiday_details["holiday_date"] = args[3]
    return holiday_details

holiday = datetime.strptime('2022-01-18', '%Y-%m-%d')
print(set_holiday_nairobi(45678902,"Abroad","Visist to Narobi",holiday))

def identifier(function):
    """ to check whether the term id
    is present in the input that denotes that the input value is an identifier of
    any kind and returns the numerical value of the identifier by removing its prefix.
    """
    def decorate_id(*args):
        """ This decorator will be added to a function to
    set promotion details for any input product for the Nairobi branch.
    """
        arguments = []
        for arg in args:
            if isinstance(arg, str):
                arg = arg.lower()
                if "id" in arg:
                    arg = int(''.join(filter(str.isdigit,arg)))
            arguments.append(arg)
        return function(*args)
    return decorate_id

@identifier
def set_promotion_nairobi(*args):
    """set variables for the product promotion details of the Malibu branch and it takes
    in the arguments using *args similar to the set_holiday_nairobi function. The first
    argument of this function will be set as branch_id , the second argument as product_id ,
    the third argument as promotion_date, the fourth as promotion_type, and the fifth as
    promotion_reason. All of these input arguments are also converted into a dictionary variable
    by the function and it returns the dictionary with its key-value pairs denoting each value.
    There are two id arguments in this function that get decorated by the identifier.
    """
    promotion_details = {}
    promotion_details["branch_id"] = args[0]
    promotion_details["promotion_type"] = args[1]
    promotion_details["promotion_name"] = args[2]
    promotion_details['promotion_reason'] = args[4]
    promotion_details["promotion_date"] = args[3]
    return promotion_details

promotion_date = datetime.strptime('2022-12-23', '%Y-%m-%d')
print("\n ******************************Second function => promotion *********\n")
print(set_promotion_nairobi(45678902,"Abroad","Visist to Narobi",
                            "Doing great job",promotion_date))
