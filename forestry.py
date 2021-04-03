import random
import numpy as np

class clearing():
    def __init__(self, calories, growthMean, growthSD):
        self.calories = calories
        self.growthMean = growthMean
        self.growthSD = growthSD
        self.birds = []
    
    def growth(self):
        # Growth of the forest in a single day 
        self.calories += np.random.normal(loc=self.growthMean, scale=self.growthSD, size=1)
    
    def resolve(self):
        # Call birds[0].aggresion(birds[1]), which should be a function to resolve calorie values 
        # Should also return the loss of calories in the clearing. The proportion that the birds graze on 
        # should be determined by the user
        return 0
    
    def time(self):
        # A day passes in the forest 
        self.resolve()
        self.growth()


class forest():
    def __init__(self, totalSpaces):
        self.totalSpaces = totalSpaces
        self.spaces = []
        self.allBirds = []
        self.nonOccupiedBirds = []
    
    def load(self, allBirds):
        self.allBirds = allBirds
    
    def occupy(self):
        # Distribute the birds across the spaces 
        return 0

newClearing = clearing(10, 0, 1)
newClearing.growth()
