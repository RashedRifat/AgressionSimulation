try:
    import random as random
    import numpy as np
except:
    raise ImportError("Unable to import required modules. Please install the requirements.txt file.")

class clearing():
    def __init__(self, calories, growthMean, growthSD, consumePerMeal=0.7, simulation_logger=None):
        self.calories = calories
        self.growthMean = growthMean
        self.growthSD = growthSD
        self.consumePerMeal = consumePerMeal
        self.birds = []
        self.simulation_logger = simulation_logger

    def occupy(self, bird1, bird2):
        self.birds = [bird1, bird2]
    
    def growth(self):
        # Growth of the clearing in a single day 
        self.calories += int(np.random.normal(loc=self.growthMean, scale=self.growthSD, size=1))
    
    def resolve(self):
        # Resolves the agression between two birds and checks for procreation 
        # Only part of the clearings calories are consumed 

        partialCalories = self.calories * self.consumePerMeal
        self.calories -= partialCalories
        self.birds[0].aggresion(self.birds[1], partialCalories)

        return self.birds[0].procreate(self.birds[1])
    
    def time(self):
        # A day passes in the clearing
        # This function returns the new children, if generated 

        # Let time pass for each bird and log results 
        for bird in self.birds:
            bird.time()
            self.simulation_logger.add(bird)

        # Resolve aggression, procreation and clearing growth. Log the child (if there is a child). 
        children = self.resolve()
        for bird in children:
            self.simulation_logger.add(bird, child=True)
        self.growth()

        return children

class forest():
    def __init__(self, totalSpaces, calorieMean, calorieSD, growthMean, growthSD, simulation_logger=None):
        self.totalSpaces = totalSpaces
        self.spaces = []
        self.allBirds = []
        self.nonOccupiedBirds = []
        self.simulation_logger = simulation_logger
    
    def load(self, allBirds):
        self.allBirds = allBirds
    
    def occupy(self):
        # Distribute the birds randomly across the spaces 
        # Birds that did not find a clearing should be added to the nonOccupiedBirds territory
        
        return 0

    def time(self):
        # Should distribute all of the allBirds array into the clearings 
        # Should call the time function on all environments, currently supporting only the forest 
        # Finally, update the allBirds array to reflect the changes (birth/death) of these birds 

        return 0

newClearing = clearing(10, 0, 1)
newClearing.growth()

# TODO: Test clearing and forestry code using a simulation_logger