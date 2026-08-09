
class ChaiCup :
    size = 150

    def describe(self) :
        return f"A {self.size} ml chai  cup"


cup = ChaiCup()
print(ChaiCup.describe(cup))

cup.size = 100
print(ChaiCup.describe(cup))

cup_two = ChaiCup()
cup_two.size = 200

print(cup_two.describe())
print(ChaiCup.describe(cup_two))