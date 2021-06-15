try:
    import random as random
    import agressionSimulation as sim 
    from tqdm import tqdm 
except ImportError as ex:
    raise ImportError("Unable to import required modules. Please install the requirements.txt file.\n" + ex.with_traceback())

class ecosystem():
    # This class represents the ecosystem in which birds and the forest is stored 
    # You can spawn the birds, the forest and simulate a day passing. 

    def __init__(self, simulation_logger):
        self.doves = 0
        self.hawks = 0
        self.allBirds = []
        self.forest = None
        self.sl = simulation_logger
    
    def numOfDoves(self):
        return self.doves
    
    def numOfHawks(self):
        return self.hawks
    
    def totalPopulation(self):
        return self.doves + self.hawks 
    
    def spawnBirds(self, total, dovePercent, startingCalories, calorieLimit, dailySpend, malePercent=0.5):
        # Spawn the birds according to the input variables 

        # Basic error checking 
        if not isinstance(dovePercent, (int, float)) or not (0 <= dovePercent <= 1):
            raise ValueError(f"dovePercent shoould be an integer between 0 and 1 not {dovePercent}")
        if not isinstance(malePercent, (int, float)) or not (0 <= malePercent <= 1):
            raise ValueError(f"malePercent shoould be an integer between 0 and 1 not {malePercent}")
       
        for id in range(0, total):
            # get random species according to malePercent
            newBird = sim.bird(str(id))
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
            newBird.calories = startingCalories
            newBird.calorieLimit = calorieLimit
            newBird.dailySpend = dailySpend

            self.allBirds.append(newBird)
        
        self.sl.new_day()
        self.sl.increment(num_of_doves=self.numOfDoves(), num_of_hawks=self.numOfHawks())
        
    def spawnForest(self, totalSpaces, calorieMean, calorieSD, growthMean, growthSD, max_search=3):

        # Create a forest class that contains a normal distribution of food
        # with a normal distribution of growth (perhaps create a second distribution and add it to the first)
        self.forest = sim.forest(totalSpaces, calorieMean, calorieSD, growthMean, growthSD, self.sl, 3)
        self.forest.load(self.allBirds)


    def time(self, days=1):
        # A day passes in the ecosystem, with the time function called for all envrionments, (currently only the forest class)
        # Record all of the days events within the logger 

        for _ in tqdm(range(0, days), desc="Simulating agression...", unit=" days", ncols=100, 
                                        total=days, maxinterval=1):
            self.sl.new_day()
            self.forest.time()
    
    def save_results(self, filename, preview=False):
        # Save the results of the simulation

        self.sl.save(filename=filename)
        print(f"\nSaved results to results//{filename}")

        if preview:
            print("Preview of results: ")
            self.show_results()
    
    def show_results(self, n=5):
        # Show the results of the simulation 

        self.sl.show(n=n)
    
    def make_population_graph(self, filename=""):
        print(self.sl.make_population_graph(filename))
    
    def make_bird_population_graph(self, filename=""):
        print(self.sl.make_bird_population_graph(filename))

    def make_calorie_graph(self, filename=""):
        print(self.sl.make_calorie_graph(filename))
    
    def make_all_graphs(self):
        self.make_bird_population_graph()
        self.make_population_graph()
        self.make_calorie_graph()