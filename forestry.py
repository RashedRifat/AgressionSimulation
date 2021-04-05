try:
    import random as random
    import numpy as np
except:
    raise ImportError("Unable to import required modules. Please install the requirements.txt file.")

class clearing():
    def __init__(self, calories, growthMean, growthSD):
        self.calories = calories
        self.growthMean = growthMean
        self.growthSD = growthSD
        self.birds = []

    def occupy(self, bird1, bird2):
        self.birds = [bird1, bird2]
    
    def growth(self):
        # Growth of the clearing in a single day 
        self.calories += np.random.normal(loc=self.growthMean, scale=self.growthSD, size=1)
    
    def resolve(self):
        # Call birds[0].aggresion(birds[1]), which should be a function to resolve calorie values 
        # Should also return the loss of calories in the clearing. The proportion that the birds graze on 
        # should be determined by the user
        # Should also call the procreate function for these birds and return the birds that are alive, including births


        return []
    
    def time(self):
        # A day passes in the clearing
        # Call bird.time() function and update the results into a Pandas DataFrame, via a logger object
        # Should return an array of birds that survived/were born from the resolve function

        self.resolve()
        self.growth()
        return []


class forest():
    def __init__(self, totalSpaces, calorieMean, calorieSD, growthMean, growthSD):
        self.totalSpaces = totalSpaces
        self.spaces = []
        self.allBirds = []
        self.nonOccupiedBirds = []
    
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
