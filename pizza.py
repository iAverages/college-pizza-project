class Pizza:

    def __init__(self, id, name, toppings, price) -> None:
        self.id = id
        self.name = name
        self.toppings = toppings
        self.price = price
        pass

    def toString(self):
        # print(self.toppings)
        toppings = ", ".join(self.toppings)
        return f"{self.name} | {toppings} | {self.price}"
    
    def getID(self):
        return self.id