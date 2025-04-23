
class SimpleClass:
    ...

class Animal:
        ...

class Classey:
    var = 2

    def method(self):
        print(self.var)

object_one = Classey()
object_two = Classey()

object_one.varia = 3
object_two.varia = 5

print(object_one.varia)
print(object_one.varia)

class Transport:
    def __init__(self, air, water):
        self.air = air
        self.water = water


trans_obj = Transport("beluga", "aircraft")
trans_obj2 = Transport("jet", "water")


print(trans_obj.water)


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

x = Person("John", "Doe")
x.printname()



