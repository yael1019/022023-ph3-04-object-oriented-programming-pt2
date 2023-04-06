# Object Oriented Programming - Inheritance, Decorators, and Class Methods/Variables

## Learning Goals

- Object inheritance

- Super

- Decorators

- Class variables

- Class methods

- Bonus: Building your own decorator

- Bonus: Lambdas

## Decorator Example:

```py
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
```

## Lambda Example:

```py
add = lambda x,y: x + y
```
