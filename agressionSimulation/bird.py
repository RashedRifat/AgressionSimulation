try:
    import random 
    import agressionSimulation as sim 
except ImportError as ex:
    raise ImportError("Unable to import required modules. Please install the requirements.txt file.\n" + ex.with_traceback())

NoneType = type(None)

class bird():
    ''' 
        Author: Rashed Rifat
        This class represents a bird within the simulation. 
        A bird has a specific ID, species, gender, calories, a calorie limit, daily expenditure needed to stay alive and a set number of starting calories. 
    '''

    # This class represents a single bird in an ecosystem  

    def __init__(self, id):
        self.isSet = False
        self.species = ""
        self.gender = ""
        self.calories = 0
        self.calorieLimit = 0
        self.dailySpend = 0
        self.alive = True
        self.startingCalories = 0 
        self.id = id
    
    def setBirdChars(self, species, gender, startingCalories, calorieLimit, dailySpend):
        '''
            Sets the characters for a bird. 

            Parameters:
                species (str):                  the species of the bird, either a hawk or a dove (H/D) 
                gender (str):                   the gender of the bird, either male or female (M?F)
                startingCalories (int):         the number of calories a bird starts with 
                calorieLimit (int):             the total number of calories a bird can possess 
                dailySpend (int):               the minimum number of calories a bird needs to expned to stay alive and perform actions 
        '''

        # Set bird characteristics 
        self.species = species.upper()
        self.gender = gender.upper()
        self.calories = startingCalories
        self.startingCalories = startingCalories

        # Set caloric limits and spending  
        self.calorieLimit = calorieLimit
        self.dailySpend = dailySpend

        self.alive = True

    def time(self):
        '''
            Simulates time passing for a bird by spending the minmum required number of calories. 
            If a bird has negative calories, it dies and cannot perform any more actions. 
        '''  

        self.calories -= self.dailySpend
        if self.calories < 0:
            self.alive = False
    
    def isDove(self):
        '''
            Identifies if a bird is a dove. 

            Returns: 
                bool: True if a bird is a dove, else False
        '''

        if self.species == "D":
            return True
        return False
    
    def isHawk(self):
        '''
            Identifies if a bird is a hawk. 

            Returns: 
                bool: True if a bird is a hawk, else False
        '''
        if self.species == "H":
            return True
        return False
    
    def isMale(self):
        '''
            Identifies if a bird is male. 

            Returns: 
                bool: True if a bird is male, else False
        '''

        if self.gender == "M":
            return True
        return False
    
    def isFemale(self):
        '''
            Identifies if a bird is female. 

            Returns: 
                bool: True if a bird is female, else False
        '''

        if self.gender == "F":
            return True
        return False
    
    def addCalories(self, cals):
        '''
            Adds calories to a bird. 

            Parameters:
                cals (int):         the number of calories to add 
        '''

        if not isinstance(cals, (int, float)) or cals < 0:
            raise ValueError("cals should be an integer greater than 0")

        self.calories += cals
        if self.calories > self.calorieLimit:
            self.calories = self.calorieLimit
    
    def aggresion(self, other, totalCalories):
        '''
            Simulates a fight between two different birds, as dependent on their species, for some number of calories. 
            
            Parameters:
                other (bird):               the bird with which to aggress
                totalCalories (int):        the total number of calories to distribute to the two birds
        '''

        if not isinstance(other, (bird, NoneType)):
            raise TypeError("other should be a bird object!")
        
        if not isinstance(totalCalories, (int, float)) or totalCalories < 0:
            return
        
        # If there is no opposing bird 
        if other == None:
            self.addCalories(totalCalories)
            return 

        # Resolve the aggresion between two birds 
        if not self.alive or not other.alive:
            return 

        # Check to see if both birds are of the same species 
        if self.species == other.species:

            # If both are doves, distribute calories equally 
            if self.isDove():
                self.addCalories(totalCalories * 0.5)
                other.addCalories(totalCalories * 0.5)

            # if both are hawks, simulate random fight and distrbute unequally 
            if self.isHawk():
                if random.randint(1, 10) <= 5:
                    self.addCalories(totalCalories * 0.7)
                    other.addCalories(totalCalories * 0.3)
                else:
                    self.addCalories(totalCalories * 0.3)
                    other.addCalories(totalCalories * 0.7)

        # If both are unequal, distribute unequally 
        else:
            if self.isDove():
                self.addCalories(totalCalories * 0.3)
                other.addCalories(totalCalories * 0.7)
            else:
                self.addCalories(totalCalories * 0.7)
                other.addCalories(totalCalories * 0.3)
        
    
    def procreate(self, other):
        '''
            Attempts to simulate the procreation of a new bird from two parent birds. 

            Parameters:
                other (sim.bird):       the second parent 

            Returns
                offspring (sim.bird):       the offspring of the two birds
        '''
        # Check to see if both birds can procreate and return array with results

        if not isinstance(other, (bird, NoneType)):
            raise TypeError("bird should be a bird object!")

        if other == None:
            return []

        if not self.alive or not other.alive:
            return []

        if self.gender == other.gender or self.species != other.species:
            return []
        
        offspring = bird("[" + str(self.id) + " | " + str(other.id) + "]")
        offspring_gender = "M" if random.random() < 0.5 else "F"
        offspring.setBirdChars(self.species, offspring_gender, self.startingCalories, self.calorieLimit, self.dailySpend)
        offspring.alive = True
        offspring.calories = self.startingCalories
        return [offspring]
    
    def show(self):
        '''
            Returns a string representation of a bird 

            Returns:
                to_string (str):        a string representation of a bird
        '''

        to_string = f"Id: {self.id} | Status: {self.alive} | Bird Gender: {self.gender} | Bird Species: {self.species}"
        return to_string