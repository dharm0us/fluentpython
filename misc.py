class HauntedBus:
    """A bus model haunted by ghost passengers"""

    def __init__(self, passengers=[]):
        # when the module is loaded, defaults are set as attributes for this method, and the same list is referenced by all the objects
        # the right thing is to use None as default
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

bus1 = HauntedBus(["Akram", "Cheema"])
bus1.pick("Bhola")
print(bus1.passengers)

bus2 = HauntedBus()
bus2.pick("Dave")
print(bus2.passengers)

bus3 = HauntedBus()
bus3.pick("Esmail")
print(bus3.passengers)

print(dir(HauntedBus.__init__))
print(HauntedBus.__init__.__defaults__)