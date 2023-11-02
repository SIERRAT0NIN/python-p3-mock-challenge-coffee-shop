from statistics import mean


class Coffee:
    #! Include all=[] to every class. remove if unnecessary
    all = []

    #! 'self' is what ever called the Coffee class. example: cup_of-coffee = Coffee()

    def __init__(self, name):
        #! we are setting the name of self "self.name" to equal name, which is inputted by the user.
        self.name = name
        #! type(self).all.append(self) will add the
        type(self).all.append(self)  #!type(self)

    #! we are creating a Property, which is our getter. under the @property, we define what that property is.
    @property  # getter
    def name(self):
        #! We us _name because it is private.
        return self._name

    #! we reuse the 'name' and add '.setter' to create the setter function
    @name.setter  # setter
    def name(self, new_name):
        #! "If {new_name} instance is not a string, then raise a TypeError("error")"
        if not isinstance(new_name, str):
            raise TypeError("Coffee name must be of type String")
        #! "Or else if the {new_name}'s length is less than or equal to 3, then raise ValueError("value error")"
        #! If the new name is less than 3 charaters long, it is true, so run the error. If the new name is greater than 3 charaters, then run the follow block of code.
        elif len(new_name) <= 3:
            raise ValueError("Coffee name must be 3 charaters")
        #! Or else if self has the attribute "name", then raise the error because it already exist.
        elif hasattr(self, "name"):
            raise AttributeError("Coffee name cannot be changed after initialization")
        else:
            #! If the new_name is not in the list, then set the new_name in the list
            self._name = new_name

    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        return mean([order.price for order in self.orders()])


class Customer:
    all = []  #! We add the all = [] to all the classes, remove if not needed

    def __init__(
        self, name
    ):  #! When  the Customer class is called, "Initialize this name"
        #! self.name = *blank*
        self.name = name  #! self.name is now whatever the user input
        type(self).all.append(self)  # ? type(self)?

    #! Then we append 'self' to 'all' that was created at the top of the class.

    # ? How do I know I need to create a property
    @property  # getter #! Create a property when the class needs to be controlled."V" The Customer Class and the Coffee Class will both be controlled by the Order Class
    def name(self):
        #! We create a function that returns itself, but with a _name instead, because it is private.
        return self._name

    #! Use the getter name, in this case 'name'
    @name.setter  # setter
    def name(self, name):  #! We want to add the name to the 'all = []' created above
        if not isinstance(name, str):  #! We are checking if the instance is a string.
            #!"If the instance of name is not a string, then raise a TypeError"
            raise TypeError("Customer name must be of type String")
        elif not 1 <= len(name) <= 15:
            raise ValueError("Customer must be between 1-15")
        else:
            self._name = name

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)


class Order:
    all = []  #! Add all=[] to all classes, removed if unessarry

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)

    @property  # getter
    def customer(self):
        return self._customer

    @customer.setter  # setter
    def customer(self, new_cust):
        if not isinstance(new_cust, Customer):
            raise TypeError("Customer must be of type Customer class.")
        else:
            self._customer = new_cust

    @property  # getter
    def coffee(self):
        return self._coffee

    @coffee.setter  # setter
    def coffee(self, new_coffee):
        if not isinstance(new_coffee, Coffee):
            raise TypeError("Coffee name must be of type Coffee class.")
        else:
            self._coffee = new_coffee

    @property  # getter
    def price(self):
        return self._price

    @price.setter  # setter
    def price(self, new_price):
        if not isinstance(new_price, float):
            raise TypeError("Price must be of type Float.")
        elif not 1.0 <= new_price <= 10.0:
            raise ValueError("Price must be a number between 1.0 and 10.0")
        elif hasattr(self, "price"):
            raise AttributeError("Coffee name cannot be changed after initialization")
        else:
            self._price = new_price
