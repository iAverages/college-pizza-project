from order import Order
from utils.utils import Utils
from utils.PromptSection import Section
from utils.Prompt import Prompt

ORDERS_FILE = "data/orders.json"
class OrderManager: 

    def __init__(self, app) -> None:
        self.app = app

    def createNewOrder(self):
            order = Order()
            while True:
                id = Utils.getIntInput("Enter the ID of the Pizza you want")
                pizza = self.app.getPizza(id)
                if not pizza:
                    print("That is not a valid pizza!")
                    continue
                order.addPizza(pizza)
                if len(order.items) >= 20:
                    print("You have reached the maximum amount of Pizzas you can order at one time.")
                    break
                addAnother = Utils.getYesNoInput("Add another pizza to the order?")
                if not addAnother:
                    break

            print(f"You have added {len(order.items)} pizzas to your order.")
            name = Utils.getStringInput("What is your name?")
            address = Utils.getStringInput("What adress will the pizzas be delivered to?")
            # TODO: Add mobile number validation
            mobileNumber = Utils.getIntInput("What is your mobile number?")

            order.setCustomer([name, address, mobileNumber])
            order.setAddress(address)

            self.printOrderSummary(order)
            self.logOrder(order)


    def logOrder(self, order):
        Utils.appendJSONFile(ORDERS_FILE, order.toJSON())

    def printOrderSummary(self, order):
        prompt = Prompt()
        items = Section(6)
        
        for i in range(len(order.items)):
            item = order.items[i]
            toppings = ", ".join(item.toppings);
            items.addText(f"{i+1}. £{item.price} | {item.name} | {toppings}")

        items.addBlank()
        extraInfo = Section(4)
        extraInfo.addText(f"Discounts: {' | '.join(order.getDiscounts())}")
        extraInfo.addText(f"Fees: {' | '.join(order.getFees())} ")
        extraInfo.addText(f"Total Cost: £{order.getPrice()}")

        prompt.addText("Order Summary:")
        prompt.addBlank()
        prompt.addText("Items:", 4)
        prompt.addSection(items)
        prompt.addSection(extraInfo)

        print(prompt.build())