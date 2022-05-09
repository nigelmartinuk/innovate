class Person :
    def __init__(self, name, age, height) -> None:
        self.name = name
        self.age = age
        self.height = height

    def print(self):
        print(f"Name:{self.name} Age:{self.age} Height:{self.height}")