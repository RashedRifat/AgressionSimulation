try:
    import random as random
    import numpy as np
    import agressionSimulation as sim
except ImportError as ex:
    raise ImportError("Unable to import required modules. Please install the requirements.txt file.\n" + ex.with_traceback())

NoneType = type(None)

class clearing():
    '''
        Author: Rashed Rifat 
        This class represents a clearing within a forest, a place for birds to gather food and procreate. 
    '''
    
    def __init__(self, calories, growthMean, growthSD, simulation_logger, consumePerMeal=0.7,):
        self.calories = calories
        self.growthMean = growthMean
        self.growthSD = growthSD
        self.consumePerMeal = consumePerMeal
        self.birds = []
        self.sl = simulation_logger
    
    def occupy(self, bird1):
        '''
            Allows a bird into the clearing. 
            Params:
                bird1 (sim.bird):       the bird to add to this clearing
        '''

        if not isinstance(bird1, sim.bird):
            raise TypeError("bird1 should not be none")
        
        if len(self.birds) == 2:
            raise ValueError("Cannot occupy, clearing is full")
        
        self.birds.append(bird1)
    
    def growth(self):
        '''
            Grows the calories of a clearing by some random value drawn from a normal distribution.
        '''

        self.calories += int(np.random.normal(loc=self.growthMean, scale=self.growthSD, size=1))
    
    def resolve(self):
        '''
            Resolves the distirbution of food to the birds within this clearing, as well as procreation.     
        '''

        partialCalories = self.calories * self.consumePerMeal
        self.calories -= partialCalories

        if len(self.birds) == 1:
            self.birds[0].aggresion(None, partialCalories)
            return []
        elif len(self.birds) == 2:
                self.birds[0].aggresion(self.birds[1], partialCalories)
                return self.birds[0].procreate(self.birds[1])
        else:
            return []

    def reset(self):
        ''' 
            Resets the birds stored within the clearing to None. 
        '''

        self.birds = []
    
    def time(self):
        '''
            Simulates a day passing within the forest and logs the results within the logger. 
        '''

        old_cals = self.calories

        # Let time pass for each bird and log results 
        for bird in self.birds:
            if bird is None:
                continue
            self.sl.add(bird, child=False)
            bird.time()

        # Resolve aggression, procreation and clearing growth. Log the child (if there is a child). 
        children = self.resolve()
        if len(children) != 0:
            self.sl.add(bird, child=True)
       
        self.growth()
        new_cals = self.calories

        # Add the value of the calories to the correct environment 
        self.sl.add_space(data=[old_cals, new_cals])
        return children

class forest():
    ''' 
        Author: Rashed Rifat 
        This class represents a forest wehre the simulation takes place. A forest has multiple clearings 
        where birds can either fight for/share food and procreate. 
    '''

    def __init__(self, totalSpaces, calorieMean, calorieSD, growthMean, growthSD, simulation_logger, maxSearch=3):
        self.totalSpaces = totalSpaces
        self.spaces = []
        self.allBirds = []
        self.nonOccupiedBirds = []
        self.maxSearch = maxSearch
        self.calorieMean = calorieMean
        self.calorieSD = calorieSD
        self.growthMean = growthMean
        self.growthSD = growthSD
        self.sl = simulation_logger
    
    def load(self, allBirds):
        '''
            Loads a list of birds into the forest and creates all the spaces within the forest. 
            Params:
                allBirds (list of sim.bird objects):        the set of birds with which to run the simulation 
        '''

        self.allBirds = allBirds

        # Create all spaces  
        for i in range(0, self.totalSpaces):
            calories = int(np.random.normal(loc=self.calorieMean, scale=self.calorieSD, size=1))
            self.spaces.append(clearing(calories, self.growthMean, self.growthSD, self.sl))           
    
    def occupy(self):
        '''
            Simulates the distribution of birds within the forest to the different clearings. 
        '''


        # Shuffle all the birds 
        random.shuffle(self.allBirds)
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
                    break
                except:
                    continue 

            # If they failed more than they could, add them to the non-allocated list 
            if maxSearchCounter > self.maxSearch:
                self.nonOccupiedBirds.append(bird)
            
            birdCounter += 1
            

    def time(self):
        '''
            Simulates a day passing within the forest, recording the changes to the simulation logger. 
        '''

        self.occupy()

        # Should call the time function on all clearings, adding new birds to the total birds list 
        for clring in self.spaces:
            possibleChild = clring.time()
            if len(possibleChild) != 0:
                self.allBirds.extend(possibleChild)
            for bird in clring.birds:
                if not bird.alive:
                    self.allBirds.remove(bird)
                    del bird

            clring.reset()

        # Finally, process all the birds in the non-occupied list 
        for bird in self.nonOccupiedBirds:
            bird.time()
            self.sl.add(bird)
            if not bird.alive:
                self.allBirds.remove(bird)
                del bird
        
        # Reset the list
        self.nonOccupiedBirds = []