class Car:

    wheels=4

    def __init__(self, style, color):
        self.color=color
        self.style=style

c=Car('BMW', 'Black')

print(c.style)
print(c.color)