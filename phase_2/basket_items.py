class Basket:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]


basket = Basket(["Apple", "Banana", "Orange", "Mango"])

print("Total Items:", len(basket))

for item in basket:
    print(item)