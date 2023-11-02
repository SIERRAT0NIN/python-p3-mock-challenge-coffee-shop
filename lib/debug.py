#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

cust1 = Customer("Alberto")
cust2 = Customer("Kat")
cust3 = Customer("Anthony")
cust3 = Customer("Austin")

coffee1 = Coffee("Latte")
coffee2 = Coffee("Drip")
coffee3 = Coffee("Cappicino")

order1 = Order(cust1, coffee1, 5.0)
order2 = Order(cust2, coffee2, 10.0)
order3 = Order(cust3, coffee3, 8.0)

if __name__ == "__main__":
    print("HELLO! :) let's debug")


print("Break")
# ipdb.set_trace()
