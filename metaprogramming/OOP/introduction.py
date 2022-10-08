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
