
class TeaLeaf :
    def __init__(self, age):
        self._age = age

    @property
    def age(self) :
        return self._age + 2 


    @age.setter
    def age(self, age) :
        if 1<= age <= 10:
            self._age = age 
        else :
            raise ValueError("Age must be between 1 too 10")


leaf = TeaLeaf(2)
print(leaf.age)

leaf._age = 6
print(leaf.age)