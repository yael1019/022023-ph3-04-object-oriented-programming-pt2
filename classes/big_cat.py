# from .animal import Animal <- this is a relative import, it works aswell
# we are starting from this current file
# this is an absolute path: we are starting from the index file
from classes.animal import Animal

# we pass in the class animal as an argument which will allow us to use fn's from Animal
# this will make Animal a superclass and BigCat a subclass
# this is inheritance 
class BigCat(Animal):
    def __init__(self, name, recent_food):
        print('We are in BigCat')
        super().__init__(name, recent_food)
        print('We are leaving BigCat')

    def __repr__(self):
        return f"<BigCat name={self.name} >"

teddy = BigCat('Teddy', 'Bob the raccoon')
# => return <Animal name = Teddy >
# this inherits from Animals
teddy.recent_food
# => Bob the raccoon

# after adding repr fn:
