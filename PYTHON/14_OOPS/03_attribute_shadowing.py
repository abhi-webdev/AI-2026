class Chai :
    temperature = "hot"
    strength = "strong"

cutting = Chai()

print(cutting.temperature)
cutting.temperature = "mild"
cutting.cup = "Small"
print(cutting.temperature)
print(f"Cup size is : {cutting.cup}")


del cutting.temperature   # after deletion the attributes check in the class, if there then it fall back to the class otherwise it gives error
del cutting.cup

print(cutting.temperature)
print(f"{cutting.cup}")