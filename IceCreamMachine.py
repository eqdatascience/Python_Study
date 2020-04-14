# Implement the IceCreamMachine's scoops method so that it returns all combinations of one ingredient and one topping.
# If there are no ingredients or toppings, the method should return an empty list.


class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        res = []
        for ingredient in self.ingredients:
            for topping in self.toppings:
                res.append([ingredient, topping])
        return res


if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print(machine.scoops())  # should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
