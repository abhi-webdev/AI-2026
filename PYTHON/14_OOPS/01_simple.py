
class Chai :
    pass

class ChaiTime:
    pass

print(type(Chai))
print(type(Chai()))


ginger_tea = Chai()   # ginger_tea is the object of class Chai

print(type(ginger_tea))

print(type(ginger_tea) is Chai)
print(type(ginger_tea) is ChaiTime)


# class Engine :
#     horsepower = "150 HP Engine"
    
#     def get_engine_info(self) :
#         return self.horsepower

# ans = Engine()

# print(ans.get_engine_info())