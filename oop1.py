
# class SimpleClass:
#     ...
#
# class Animal:
#         ...
#
# class Classey:
#     var = 2
#
#     def method(self):
#         print(self.var)
#
# object_one = Classey()
# object_two = Classey()
#
# object_one.varia = 3
# object_two.varia = 5
#
# print(object_one.varia)
# print(object_one.varia)
#
# class Transport:
#     def __init__(self, air, water):
#         self.air = air
#         self.water = water
#
#
# trans_obj = Transport("beluga", "aircraft")
# trans_obj2 = Transport("jet", "water")
#
#
# print(trans_obj.water)
#
#
# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#
#     def printname(self):
#         print(self.fname, self.lname)
#
# x = Person("John", "Doe")
# x.printname()

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, qty):
        item = {item_name, qty}

        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total

cart = ShoppingCart()
# add items to our cart
cart.add_item("kiwi", 100 )
cart.add_item("papaya", 200 )
cart.add_item("orange", 78 )

print("current items in our list")
for item in cart.items:
    print( item[0],"-",item[1])

total_qty = cart.calculate_total()
print("Total Quantity: ", total_qty)


