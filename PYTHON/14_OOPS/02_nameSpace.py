
class Chai :
    origin = "India"
print(Chai.origin)

Chai.is_hot = True
print(Chai.is_hot)


print(f"After changing the value of class properties")
masala = Chai()
masala.origin = "Assam, India"
masala.is_hot = False

print(Chai.is_hot)
print(Chai.origin)

print(f"Masala: {masala.origin}")
print(f"Masala: {masala.is_hot}")


#  NameSapce in python has their own feature, It does not affect any value of another object and the class also