def my_decorator(func):
    # make and return a func inside of decorator 
    # *args is the arguments, we want to be able to pass in any number amount of args
    # and **kargs are key args
        # when you invoke the function and pass in a key with a value it is a key arg
        # whatever(name = 'bob')
    def wrapper(*args, **kwargs):
        print("Decorator is happening")
        # pass in the *args and **kargs to the function 
        # in our lion class we are calling the wrapper function passing in 2 arguments
        return func(*args, **kwargs)
        print("Decorator is happening again")
    return wrapper

# this pie operator will pass in whatever into the my_decorator 
# so when it calls func(), it will call whatever()
# to run this you call whatever(), the decorator causes this to call my_decorator passing in whatever as a cb
@my_decorator
def whatever():
    print('whatever')

# the pie tag needs to match the title of the function we declared 
@my_decorator
def something():
    print('something')

# the long way of making a deocrator
def another_func():
    print('I am another func')

another_func2 = my_decorator(another_func)
# this has everything to do with the fact that python function are 'first class functions'
# once we define a function we can pass it like any common variable

# for decorators that involve functions with arguments you can give the wrapper and func:
# (*args, **kwargs)
