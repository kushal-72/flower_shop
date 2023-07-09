class FlowerShop:
    def __init__(self):
        self.flower_stock = {}

    def add_flower(self, flower, quantity):
        if flower.name in self.flower_stock:
            self.flower_stock[flower.name].update_quantity(quantity)
        else:
            self.flower_stock[flower.name] = flower

    def remove_flower(self, flower, quantity):
        if flower.name in self.flower_stock:
            stock = self.flower_stock[flower.name]
            if stock.quantity > quantity:
                stock.update_quantity(-quantity)
            else:
                del self.flower_stock[flower.name]
        else:
            print(f"{flower.name} is not available in the flower shop.")

    def display_flower_stock(self):
        if len(self.flower_stock) == 0:
            print("\nFlower shop is out of stock.")
        else:
            print("\nFlower shop stock:")
            for flower_name, flower in self.flower_stock.items():
                print(f"{flower_name}: {flower.quantity} available")
