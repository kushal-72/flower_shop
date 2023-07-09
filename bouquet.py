class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def remove_flower(self, flower):
        self.flowers.remove(flower)

    def get_total_price(self):
        total_price = sum(flower.price for flower in self.flowers)
        return total_price

    def display_bouquet(self):
        if len(self.flowers) == 0:
            print("\nThe bouquet is empty.")
        else:
            print("\nBouquet contains:")
            for flower in self.flowers:
                print(flower)
