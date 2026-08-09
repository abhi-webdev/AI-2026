
class BaseChai :
    def __init__(self, type_):
        self.type = type_

    def prepare (self) :
        print(f"{self.type} chai is preparing...")

class MasalaChai(BaseChai) :
    def adding_spice(self) :
        print(f"Adding Spice in {self.type} chai")


class ChaiShop :
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self) :
        print(f"{self.chai.type} serving in the shop")
        self.chai.prepare()


class FancyChaiShop(ChaiShop) :
    chai_cls = MasalaChai


shop = ChaiShop()
Fancy = FancyChaiShop()

shop.serve()
Fancy.serve()
Fancy.chai.adding_spice()



        