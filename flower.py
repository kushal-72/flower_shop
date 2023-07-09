class Flower:
    def __init__(self, name, color, price, quantity):
        self.name = name
        self.color = color
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.color} {self.name} - ${self.price}"

    def update_quantity(self, quantity):
        self.quantity += quantity
