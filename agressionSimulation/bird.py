try:
    import random 
except:
    raise ImportError("Unable to import required modules. Please install the requirements.txt file.")

NoneType = type(None)
class bird():
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
        if not isinstance(cals, (int, float)) or cals < 0:
            raise ValueError("cals should be an integer greater than 0")

        self.calories += cals
        if self.calories > self.calorieLimit:
            self.calories = self.calorieLimit
    
    def aggresion(self, other, totalCalories):
        if not isinstance(other, (bird, NoneType)):
            raise TypeError("other should be a bird object!")
        
        if not isinstance(totalCalories, (int, float)) or totalCalories < 0:
            return
            #raise ValueError("totalCalories should be greater than 0, not", totalCalories)
        
        # If there is no opposing bird 
        if other == None:
            self.addCalories(totalCalories)
            return 

        # Resolve the aggresion between two birds 
        if not self.alive or not other.alive:
            return 0 

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
        
        return 0
    
    def procreate(self, other):
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
        return [offspring]
    
    def show(self):
        to_string = f"Status: {self.alive} | Bird Gender: {self.gender} | Bird Species: {self.species}"
        return to_string