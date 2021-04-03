from birds import bird
from forestry import forest
import random

class ecosystem():
    # This class represents the ecosystem in which birds and the forest is stored 
    # You can spawn the birds, the forest and simulate a day passing. 

    def __init__(self):
        self.doves = 0
        self.hawks = 0
        self.time = 0
        self.allBirds = []
        self.forest = ""
    
    def numOfDoves(self):
        return self.doves
    
    def numOfHawks(self):
        return self.hawks
    
    def totalPopulation(self):
        return self.doves + self.hawks 
    
    def spawnBirds(self, total, dovePercent, malePercent=0.5):
        # Include error checking for dovePercent, total and malePecent
        newBird = bird()

        for elem in range(0, total):
            # get random species according to malePercent
            if random.random() <= dovePercent:
                newBird.setSpecies("D")
                self.doves += 1
            else:
                newBird.setSpecies("H")
                self.hawks += 1

            # get random gender according to malePercent
            if random.random() <= malePercent:
                newBird.setGender("M")
            else:
                newBird.setGender("F")

            self.allBirds.append(newBird)

    def spawnForest(self, totalSpace):
        # Create a forest class that contains a nsormal distribution of food
        # with a normal distribution of growth (perhaps create a second distribution and add it to the first)
        return 0


eco = ecosystem()
eco.spawnBirds(100, 0.5)
print(eco.totalPopulation(), eco.numOfDoves(), eco.numOfHawks())     