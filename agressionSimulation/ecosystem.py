try:
    import random as random
except:
    raise ImportError("Unable to import required modules. Please install the requirements.txt file.")

class ecosystem():
    # This class represents the ecosystem in which birds and the forest is stored 
    # You can spawn the birds, the forest and simulate a day passing. 

    def __init__(self, simulation_logger=None):
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
    
    def spawnBirds(self, total, dovePercent, startingCalories, calorieLimit, dailySpend, malePercent=0.5):
        # Include error checking for dovePercent, total and malePecent
        newBird = bird()

        for elem in range(0, total):
            # get random species according to malePercent
            if random.random() <= dovePercent:
                newBird.species = "D"
                self.doves += 1
            else:
                newBird.species = "H"
                self.hawks += 1

            # get random gender according to malePercent
            if random.random() <= malePercent:
                newBird.gender = "M"
            else:
                newBird.gender = "F"

            # Set caloric values 
            newBird.startingCalories = startingCalories
            newBird.calorieLimit = calorieLimit
            newBird.dailySpend = dailySpend

            self.allBirds.append(newBird)

    def spawnForest(self, totalSpaces, calorieMean, calorieSD, growthMean, growthSD):
        # Create a forest class that contains a normal distribution of food
        # with a normal distribution of growth (perhaps create a second distribution and add it to the first)
        
        return 0

    def time(self):
        # A day passes in the ecosystem, with the time function called for all envrionments, currently only the forest
        # Should call time function on the simulation_logger, creating a new day. 

        return 0


# eco = ecosystem()
# eco.spawnBirds(100, 0.5, 1000, 5000, 100)
# print(eco.totalPopulation(), eco.numOfDoves(), eco.numOfHawks())     