# from custom_decorator.my_decorator import my_decorator
from classes.big_cat import BigCat

class Lion(BigCat):

    def __init__(self, name, recent_food, mane):
        # super method represents the parent, the superclass
            # we are trying to use the parents init fn 
            # we pass the arguments that our super init fn accepts 
        print('We are in Lion')
        super().__init__(name, recent_food)
        self.mane = mane
        print('We are leaving Lion')

    # you can call this function eat, but you do not have to, it does not have to match the superclass function
    # it does not have to be the same name if you want to access that super eat fn
    def eat_foodies(self, food):
        super().eat(food)
        print('It was delishhhh')

    def __repr__(self):
        return f"<Lion name={self.name} recent_food={self.recent_food} mane={self.mane} >"

bill = Lion('Bill', 'hamster', 'BIG')
# => <Lion name = Bill recent_food = hamster mane = BIG >
