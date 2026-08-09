
class Chai :
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength


class Ginger_chai(Chai) :
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level

order = Ginger_chai("Ginger", "Hard", "Medium")

print(order.type)
print(order.strength)
print(order.spice_level)
