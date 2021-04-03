class bird():
    # This class represents a single bird in an ecosystem  

    def __init__(self):
        self.isSet = False
        self.species = ""
        self.gender = ""
        self.calories = 0
        self.calorieLimit = 0
        self.dailySpend = 0
        self.alive = True
    
    def setBirdChars(self, species, gender, startingCalories, calorieLimit, dailySpend):
        # Set bird characteristics 
        self.species = species.upper()
        self.gender = gender.upper()
        self.calories = startingCalories

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
                pass

        # If both are unequal, distribute unequally 
        else:
            pass 
        
        return 0
