#Name: Dan-Ha Le

# I. Abstract Factory

#FRUITS:
# - bananas:
class banana():
    def harvest():
        pass

class greenBanana(banana):
    def harvest():
        print ("Green banana is harvested")

class yellowBanana(banana):
    def harvest():
        print ("Yellow banana is harvested")

# - coconuts:
class coconut():
    def harvest():
        pass

class greenCoconut(coconut):
    def harvest():
        print ("Green coconut is harvested")
        
class yellowCoconut(coconut):
    def harvest():
        print ("Yellow coconut is harvested")

# JUNGLES/FACTORIES:

class Jungle():
    def getBanana():
        pass
    def getCoconut():
        pass


class JungleA(Jungle):
    def getBanana():
        return greenBanana.harvest()

    def getCoconut():
        return greenCoconut.harvest()

class JungleB(Jungle):
    def getBanana():
        return yellowBanana.harvest()
    
    def getCoconut():
        return yellowCoconut.harvest()

def main():
    #Context: Green fruits are only found in JungleA. Yellow fruits are only found in JungleB.
    #   Test: getting JungleA to produce fruits -
    print("\nHarvesting fruits from JungleA")
    JungleA.getBanana()
    JungleA.getCoconut()
    print("\nHarvesting fruits from JungleB")
    JungleB.getBanana()
    JungleB.getCoconut()
    print("\n")


main()