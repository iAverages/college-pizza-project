from pizza import Pizza
from orderManager import OrderManager
from utils.utils import Utils

PIZZAS_FILE = "pizzas.json"

class PizzaProject: 

    def __init__(self) -> None:
        self.loadPizzas()
        self.orderManager = OrderManager(self)
        self.orderManager.createNewOrder()
 
    def loadPizzas(self):
        pizzas = Utils.readJSON(PIZZAS_FILE)
        tmp = []
        self.pizzas = []
        for i in range(len(pizzas)):
            pizza = pizzas[i]
            tmp.append(Pizza(pizza["id"], pizza["name"], pizza["toppings"], pizza["cost"]))

        # Sort into the correct order by ID using insertion sort
        # Start at second index (index 1)
        for i in range (1, len(tmp)):
            currItem = tmp[i]
            prevIdx = i - 1
            # Move each element up if its ID is lower than the current Items ID
            while prevIdx >= 0 and tmp[prevIdx].getID() > currItem.getID():
                tmp[prevIdx + 1] = tmp[prevIdx]
                prevIdx -= 1
            tmp[prevIdx + 1 ] = currItem
        
        self.pizzas = tmp

    def getPizza(self, id):
        if id > len(self.pizzas) or id <= 0:
            return False
            
        pizza = self.pizzas[id - 1]
        
        # Pizzas should be loaded in the ID order,
        # But just incase they're not, loop though to find them.
        if pizza.id == id:
            return pizza
            
        for piz in self.pizzas:
            if piz.id == id:
                return piz
        return False
        
        

PizzaProject()