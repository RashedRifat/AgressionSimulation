try:
    import random 
except:
    raise ImportError("Unable to import required modules. Please install the requirements.txt file.")

class bird():
    # This class represents a single bird in an ecosystem  

    def __init__(self, simulation_logger=None):
        self.isSet = False
        self.species = ""
        self.gender = ""
        self.calories = 0
        self.calorieLimit = 0
        self.dailySpend = 0
        self.alive = True
        self.startingCalories = 0 
    
    def setBirdChars(self, species, gender, startingCalories, calorieLimit, dailySpend):
        # Set bird characteristics 
        self.species = species.upper()
        self.gender = gender.upper()
        self.calories = startingCalories
        self.startingCalories = startingCalories

        # Set caloric limits and spending  
        self.calorieLimit = calorieLimit
        self.dailySpend = dailySpend

        # keep track of it being set 
        self.isSet = True

    def time(self):
        self.calories -= self.dailySpend
        if self.calories < 0:
            self.alive = False
    
    def isDove(self):
        if self.species == "D":
            return True
        return False
    
    def isHawk(self):
        if self.species == "H":
            return True
        return False
    
    def isMale(self):
        if self.gender == "M":
            return True
        return False
    
    def isFemale(self):
        if self.gender == "F":
            return True
        return False
    
    def addCalories(self, cals):
        self.calories += cals
        if self.calories > self.calorieLimit:
            self.calories = self.calorieLimit
    
    def aggresion(self, other, totalCalories):
        # Resolve the aggresion between two birds 

        if self.gender == other.gender:

            # If both are doves, distribute calories equally 
            if self.isDove():
                self.addCalories(totalCalories * 0.5)
                other.addCalories(totalCalories * 0.5)

            # if both are hawks, simulate random fight and distrbute unequally 
            if self.isHawk():
                if random.randint(1, 10) <= 5:
                    self.addCalories(totalCalories * 0.7)
                    other.addCalories(totalCalories * 0.3)

        # If both are unequal, distribute unequally 
        else:
            if self.isDove():
                self.addCalories(totalCalories * 0.3)
                other.addCalories(totalCalories * 0.7)
            else:
                self.addCalories(totalCalories * 0.7)
                other.addCalories(totalCalories * 0.3)
        
        return 0
    
    def procreate(self, other):
        # Check to see if both birds can procreate and return array with results

        if not self.gender == other.gender:
            return []
        
        offspring = bird()
        offspring_gender = "M" if random.random() < 0.5 else "F"
        offspring.setBirdChars(self.species, offspring_gender, self.startingCalories, self.calorieLimit, self.dailySpend)
        return [offspring]

# TODO: Test Bird Code