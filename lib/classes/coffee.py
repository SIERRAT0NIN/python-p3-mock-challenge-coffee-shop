class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and name and not hasattr(self, "name"):
            self._name = name
        else:
            raise AttributeError(
                "Must be a string with at least one character and it cannot be changed"
            )

    def orders(self):
        return [order for order in Order.all if order.coffee is self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        return mean([order.price for order in self.orders()])


from classes.order import Order
from statistics import mean