def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Decorator is happening")
        return func(*args, **kwargs)
        print("Decorator is happening again")
    return wrapper

# this has everything to do with the fact that python function are 'first class functions'
# once we define a function we can pass it like any common variable

# for decorators that involve functions with arguments you can give the wrapper and func:
# (*args, **kwargs)
