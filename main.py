from bouquet import Bouquet
from flower import Flower
from flower_shop import FlowerShop

if __name__ == "__main__":
    rose = Flower("Rose", "Red", 2.5, 10)
    lily = Flower("Lily", "White", 1.8, 15)
    tulip = Flower("Tulip", "Pink", 1.2, 20)

    bouquet = Bouquet()
    bouquet.add_flower(rose)
    bouquet.add_flower(lily)
    bouquet.add_flower(tulip)

    bouquet.display_bouquet()
    print("Total price:", bouquet.get_total_price())

    flower_shop = FlowerShop()
    flower_shop.add_flower(rose, 5)
    flower_shop.add_flower(lily, 10)
    flower_shop.add_flower(tulip, 15)

    flower_shop.display_flower_stock()

    flower_shop.remove_flower(rose, 3)
    flower_shop.display_flower_stock()
