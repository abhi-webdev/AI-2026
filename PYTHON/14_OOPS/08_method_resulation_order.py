
class A :
    lebel = "This is a first level"

class B(A) :
    lebel = "This is a second level"

class C(A) :
    lebel = "This is a third level"

class D(B, C) :
    pass


cup = D()

print(cup.lebel)



# ----------- Static Methods ---------------

class ChaiUtils : 
    @staticmethod
    def chai_ingredents (text) :
        return [item.strip() for item in text.split(",")]

raw = "  water  , milk,  ginger,  honey  "


cleaned = ChaiUtils.chai_ingredents(raw)

print(cleaned)