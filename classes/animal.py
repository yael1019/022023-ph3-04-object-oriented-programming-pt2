class Animal:

    def __init__(self, name, recent_food):
        print('We are in Animal')
        self.name = name
        self.recent_food = recent_food
        print('We are leaving Animal')

    def eat(self, food):
        print(f'{self.name} is eating {food}')
        self.recent_food = food

    def __repr__(self):
        return f"<Animal name={self.name} >"

#! ////////////////////////////////////////////////////////////////////////////////
# lambda functions are anonymous functions just like arrow fn's in js
# JS:
    # () => 1 + 1
    # const empty = () => 1 + 1
# Pyhton:
# when using lambda you can omit the parenthesis
    # lambda x,y: x + y
    # add_tog = lambda x,y: x + y
#! ///////////////////////////////////////////////////////////////////////////////


