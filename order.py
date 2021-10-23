DELIVERY_FEE = 1.50
DISCOUNT = 0.8 # 20% Discount
APPLY_DISCOUNT_MIN = 20
MIN_ORDER = 9

class Order:

    items = []
    customer = None
    address = ""
    cost = 0
    
    def __init__(self) -> None:
        pass

    def setCustomer(self, customer):
        self.customer = customer

    def addPizza(self, pizza):
        self.items.append(pizza)
        self.cost += pizza.price

    def setAddress(self, address):
        self.address = address
    
    def getPrice(self):
        cost = self.cost
        if self.cost > APPLY_DISCOUNT_MIN:
            cost = self.cost * DISCOUNT
        elif self.cost < MIN_ORDER:
            cost = self.cost + DELIVERY_FEE
        
        return f"{cost:.2f}"

    def getDiscounts(self):
        discounts = []
        if self.cost > MIN_ORDER:
            discounts.append(f"Free delivery £-{DELIVERY_FEE}")
        if self.cost > APPLY_DISCOUNT_MIN:
            discounts.append("20% off orders over £20")
        return discounts if len(discounts) != 0 else ["None"]
        
    def getFees(self):
        fees = []
        if self.cost < MIN_ORDER:
            fees.append(f"£{DELIVERY_FEE} delivery fee")

        return fees if len(fees) != 0 else ["None"]

    def toJSON(self): 
        return {
            "customer": self.customer,
            "address": self.address,
            "items": [pizza.getID() for pizza in self.items],
            "cost": self.cost,
            "discounts": self.getDiscounts(),
            "fees": self.getFees()
        } 