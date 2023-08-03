#Name: Dan-Ha Le

# No. 2:  Builder

# Build cups of boba:

class Boba ():

    def __init__(self, flavour="classic", size="M", toppings=["boba"], ice=100, sugar=100):
        self.flavour = flavour
        self.size = size
        self.toppings = toppings
        self.ice = ice
        self.sugar = sugar
    
    def __new__(self, flavour, size, toppings, ice, sugar):
        print ("A {} cup of {} with {}, {} ice, {} sugar.".format(size, flavour, toppings, ice, sugar))
    
class BobaBuilder ():
    
    def __init__(self, flavour="classic", size="M", toppings=["boba"], ice=100, sugar=100):
        self.flavour = flavour
        self.size = size
        self.toppings = toppings
        self.ice = ice
        self.sugar = sugar
    
    def flavour (self, flavour):
        self.flavour = flavour
    
    def size (self, size):
        self.size = size
    
    def toppings (self, toppings):
        self.toppings = toppings
    
    def ice (self, ice):
        self.ice = ice
    
    def sugar (self, sugar):
        self.sugar = sugar
    
    def build(self):
        return Boba(self.flavour, self.size, self.toppings, self.ice, self.sugar)

class Director():

    def __init__(self, builder):
        self.builder = builder
    
    def buildDanHaOrder(builder):
        builder.flavour("Oolong")
        builder.size("L")
        builder.toppings(["boba", "boba", "boba"])
        builder.ice = 30
        builder.sugar = 50
        return builder
    
    def buildWorstOrder(builder):
        builder.flavour("Fruit")
        builder.size("S")
        builder.toppings(["red beans"])
        builder.ice = 120
        builder.sugar = 120
        return builder.build()
    
def main():
    #Context: Boba shop.
    #   Test: The builder functions shoudl return the correct cup of boba.
    #   (self, flavour="classic", size="M", toppings=["boba"], ice=100, sugar=100)
    
    #First cup: ("Jasmine", "L", ["boba, red beans"], ice = 50, sugar = 70, dinein=False) 
    origin = Boba("Jasmine", "L", ["boba", "red beans"],50, 70) 
    builder = BobaBuilder() 
    #Error: TypeError:'str' object is not callable:
    builder.flavour("Jasmine")

    #Second cup: Making Dan-Ha's favorite order using Director
    origin2 = Boba("Oolong", "L", ["boba", "boba", "boba"], 30, 50)

    


main()