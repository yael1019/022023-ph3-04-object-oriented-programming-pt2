from custom_decorator.my_decorator import my_decorator

class Lion:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Lion name={self.name} >"
