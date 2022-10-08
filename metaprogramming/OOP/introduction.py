"""A class is a collection of common attributes and methods that
    can be reused by creating instances of the class.
    By creating a class, we define it once and reuse it
    multiple times, thus avoiding redundancy.
"""

class Animal:
    """ A class of animals """
    def __init__(self, name, age, owner):
        self.name = name
        self.age = age
        self.owner = owner

    def __repr__(self) -> str:
        return f"{self.name} is my animal name"

    # Methods
    def animal_eat(self, food,tools,food_type):
        """ The eating method """
        return {
            "animal eats": {
                "food": food, "uses": tools, "food type": food_type
            }
        }

    def animal_owner(self, full_name, address, age, gender):
        """ The details of the owner of the animal """
        return {
            "The Owner": {
                "full name": full_name, "address": address,
                "age": age, "gender": gender
            }
        }
animal_one = Animal("Cat 1",23,"lester dlester")
print(animal_one)
food = animal_one.animal_eat("meat, milk, cat food","plates","cat food")
print(food)
owner_details = animal_one.animal_owner("Duke Lester","Juja, kenya", 30,"Male")
print(owner_details)

class Cat(Animal): # Inheritance
    """ A simple class inheritance ==> cat class inherit from Animal class"""

    def __init__(self, skin_color, body_size, gender):
        super().__init__(self.name,self.age,self.owner)
        self.skin_color = skin_color
        self.body_size = body_size
        self.gender = gender

    def __repr__(self) -> str:
        return self.name


class Employee:
    """ A simple class for the employee details """

    def __init__(self):
        self.details = None

    def set_emplyoee_details(self, **details):
        """ A setter method to set all the details about an employee"""
        return details

    def calculate_net_pay(self):
        """ Calculate the net pay for the employee """
        details = self.details
        tax_pay = (details["salary"] * details["tax"]) / 100
        net_pay =  details["salary"] - tax_pay
        details["tax paid"] = tax_pay
        details["net salary"] = net_pay

        return details

employee = Employee()
employee.details = employee.set_emplyoee_details(
    full_name="duke lester", age=25, location="juja", country="kenya",
    city="Nairobi", company="Lester softs Inc", salary=400000, department="IT",
    role="Software Engineer Team Lead", tax=1.5
)

print(employee.details)
print(f"\nEmployee net pay is KES {employee.calculate_net_pay()}")
