# from custom_decorator.my_decorator import my_decorator
from classes.big_cat import BigCat
from custom_decorator.my_decorator import my_decorator

class Lion(BigCat):
    # Class variable/attribute 
    # this will be directly attached to the class itself 
    # if you run Lion.proper_lion_names it will return the list
    # you can also use it in each instance
    proper_lion_names = ['Bill', 'Ted', 'Sharief', 'Patty']
    loudest_lion = None
    all_the_lions = []

    def __init__(self, name, recent_food, mane):
        # super method represents the parent, the superclass
            # we are trying to use the parents init fn 
            # we pass the arguments that our super init fn accepts 
        print('We are in Lion')
        super().__init__(name, recent_food)
        self.mane = mane
        print('We are leaving Lion')
        # we do Lion instead of self to be safe so it always affects the class not just the instance 
        Lion.add_lion(self)

    # to make somthing a class method we need to use a decorator
    # decorator adds special functionality to the function
    # decorators use pie syntax
    # we pass in cls instead self, it is the self equivilant to self
    # our instances can use these methods aswell
    @classmethod
    def list_names(cls):
        return [name + 'the Lion' for name in cls.proper_lion_names]

    @classmethod
    def add_lion(cls, lion):
        cls.all_the_lions.append(lion)

    # this is an instance method, not a class method
    # you can call this function eat, but you do not have to, it does not have to match the superclass function
    # it does not have to be the same name if you want to access that super eat fn
    @my_decorator
    def eat_foodies(self, food):
        super().eat(food)
        print('It was delishhhh')

    def __repr__(self):
        return f"<Lion name={self.name} recent_food={self.recent_food} mane={self.mane} >"

bill = Lion('Bill', 'hamster', 'BIG')
# => <Lion name = Bill recent_food = hamster mane = BIG >

bill.proper_lion_names.append('George')
# => ['Bill', 'Ted', 'Sharief', 'Patty', 'George]
Lion.proper_lion_names.append('George')
# => ['Bill', 'Ted', 'Sharief', 'Patty', 'George]
# this persists because append is destrusctive  

bill.loudest_lion = bill
bill.loudest_lion
# => <Lion name = Bill ... >
Lion.loudest_lion
# => None

bill.list_names()
# => ['Bill the Lion', 'Ted the Lion', 'Sharief the Lion', 'Patty the Lion']

Lion.list_names()
# ['Bill the Lion', 'Ted the Lion', 'Sharief the Lion', 'Patty the Lion']

