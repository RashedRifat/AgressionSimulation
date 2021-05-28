try:
    import random as random
    import numpy as np
    import agressionSimulation as sim
except:
    raise ImportError("Unable to import required modules. Please install the requirements.txt file.")

NoneType = type(None)

class clearing():
    
    def __init__(self, calories, growthMean, growthSD, consumePerMeal=0.7, simulation_logger=None):
        self.calories = calories
        self.growthMean = growthMean
        self.growthSD = growthSD
        self.consumePerMeal = consumePerMeal
        self.birds = []
        self.simulation_logger = simulation_logger

    def occupy(self, bird1, bird2):
        if not bird1 or not isinstance(bird1, sim.bird) or not isinstance(bird2, (sim.bird, NoneType)):
            raise TypeError("either bird1 or bird2 should be bird objects")

        self.birds = [bird1, bird2]
    
    def occupy(self, bird1):
        if not isinstance(bird1, sim.bird):
            raise TypeError("bird1 should not be none")
        
        if len(self.birds) == 2:
            raise ValueError("Cannot occupy, clearing is full")
        
        self.birds.append(bird1)
    
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
    
    def reset(self):
        del self.birds
        self.birds = []
    
    def time(self):
        # A day passes in the clearing
        # This function returns the new children, if generated 

        # Let time pass for each bird and log results 
        for bird in self.birds:
            if bird is None:
                continue
            bird.time()
            self.simulation_logger.add(bird)

        # Resolve aggression, procreation and clearing growth. Log the child (if there is a child). 
        children = self.resolve()
        if children:
            self.simulation_logger.add(bird, child=True)
        self.growth()

        return children

class forest():

    def __init__(self, totalSpaces, calorieMean, calorieSD, growthMean, growthSD, maxSearch=3, simulation_logger=None):
        self.totalSpaces = totalSpaces
        self.spaces = []
        self.allBirds = []
        self.nonOccupiedBirds = []
        self.maxSearch = maxSearch
        self.calorieMean = calorieMean
        self.calorieSD = calorieSD
        self.growthMean = growthMean
        self.growthSD = growthSD
        self.simulation_logger = simulation_logger
    
    def load(self, allBirds):
        self.allBirds = allBirds

        # Create all spaces  
        for i in range(0, self.totalSpaces):
            calories = int(np.random.normal(loc=self.calorieMean, scale=self.calorieSD, size=1))
            self.spaces.append(clearing(calories, self.growthMean, self.growthSD, simulation_logger=self.simulation_logger))           
    
    def occupy(self):
        # Shuffle all the birds 
        random.shuffle(self.allBirds)
        occupiedBirdCounter = 0
        birdCounter = 0

        # Iterate through the birds and attempt to add them to a clearing 
        # If they fail more than the maxSearch times, add to nonccupied list 
        for bird in self.allBirds:
            maxSearchCounter = 0

            # If the number of birds added is twice more than the number of spaces, the bird cannot be added 
            if birdCounter > self.totalSpaces * 2:
                self.nonOccupiedBirds.extend(self.allBirds[birdCounter+1:])
                break

            # The bird goes on the hunt and tries to occupy a clearing 
            while maxSearchCounter < self.maxSearch:
                maxSearchCounter += 1
                randomSpace = random.randint(0, self.totalSpaces)
                try:
                    self.spaces[randomSpace].occupy(bird)
                except:
                    continue 

            # If they failed more than they could, add them to the non-allocated list 
            if maxSearchCounter > self.maxSearch:
                self.nonOccupiedBirds.append(bird)
            
            birdCounter += 1
            

    def time(self):

        # Should call the time function on all clearings, adding new birds to the total birds list 
        for clring in self.spaces:
            possibleChild = clring.time()
            if possibleChild is not None:
                self.allBirds.extend(possibleChild)

            clring.reset()

        # Finally, process all the birds in the non-occupied list 
        for bird in self.nonOccupiedBirds:
            bird.time()
            self.simulation_logger.add(bird)
        
        # Reset the list, cleaning up memory as we go
        del self.nonOccupiedBirds
        self.nonOccupiedBirds = []
