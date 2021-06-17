try:
    import random as random
    import agressionSimulation as sim 
    from tqdm import tqdm 
except ImportError as ex:
    raise ImportError("Unable to import required modules. Please install the requirements.txt file.\n" + ex.with_traceback())

class ecosystem():
    '''
        Author: Rashed Rifat
        This class represents the ecosystem in which the simulation takes place. 
    '''

    def __init__(self, simulation_logger):
        self.doves = 0
        self.hawks = 0
        self.allBirds = []
        self.forest = None
        self.sl = simulation_logger
    
    def numOfDoves(self):
        # Returns the number of doeves within the ecosystem. 
        return self.doves
    
    def numOfHawks(self):
        # Returns the number of hawks within the ecosystem. 
        return self.hawks
    
    def totalPopulation(self):
        # Returns the number of birds within the ecosystem. 
        return self.doves + self.hawks 
    
    def spawnBirds(self, total, dovePercent, startingCalories, calorieLimit, dailySpend, malePercent=0.5):
        '''     
            Spawns all of the birds needed for the simulation 
            Params:
                total (int):                    specifies the total number of birds within the simulation         
                dovePercent (int):              specifies the percent split between hawks and doves within the simulation 
                startingCalories (int):         specifies the calories that a bird starts out with 
                calorieLimit (int):             specifies the total number of calories that a brid can have
                dailySpend (int):               specifies the daily number of calories needed for a bird to live 
                malePercent (int):              specifies the percent of males within the simulationd
        '''

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
        '''
            Spawns the forest within which this simulation takes place. 
            Params:
                totalSpaces (int):          the total number of spaces to spawn within the forest 
                calorieMean (int):          the mean number of calories that the clearings within the forest should spawn with 
                calorieSD (int):            the standard deviation by which the starting calories spawned within the forest can vary by
                growthMean (int):           the mean growth of the clearings within the forest each day
                growthSD (int):             the standard deviation of by which the growth of calories within the forest varies by 
                max_search (int):           the maximum amount of time birds can search within the forest for 
        '''

        # Create a forest class that contains a normal distribution of food
        # with a normal distribution of growth
        self.forest = sim.forest(totalSpaces, calorieMean, calorieSD, growthMean, growthSD, self.sl, max_search=max_search)
        self.forest.load(self.allBirds)


    def time(self, days=1):
        '''
            Simulate the passing of time within the ecosystem, recording all changes to the logger. 
            Params:
                days (int): the number of days for which to simulate for 
        '''

        for _ in tqdm(range(0, days), desc="Simulating agression...", unit=" days", ncols=100, 
                                        total=days, maxinterval=1):
            self.sl.new_day()
            self.forest.time()
    
    def save_results(self, filename, preview=False):
        '''
            Saves the results of the simulation to a csv file
            Params:
                filename (str):            the name of the file to save the results to 
                preview (bool):            boolean value reprsenting wether a preview of the results should be shown 
        '''

        self.sl.save(filename=filename)
        print(f"\nSaved results to results//{filename}")

        if preview:
            print("Preview of results: ")
            self.show_results()
    
    def show_results(self, n=5):
        '''' 
            Shows the results of the simulation 
            Params:
                n (int):        the number of days for which to display the results for 
        '''

        self.sl.show(n=n)
    
    def make_population_graph(self, filename=""):
        '''
            Creates a population graph of the bird population over time. 
            Params:
                filename (str):         the filename for which to save the results for 
        '''

        print(self.sl.make_population_graph(filename))
    
    def make_bird_population_graph(self, filename=""):
        '''
            Creates a bird population graph of the dove and hawk population over time. 
            Params:
                filename (str):         the filename for which to save the results for 
        '''

        print(self.sl.make_bird_population_graph(filename))

    def make_calorie_graph(self, filename=""):
        '''
            Creates a calorie graph of the ecosystem over time. 
            Params:
                filename (str):         the filename for which to save the results for 
        '''

        print(self.sl.make_calorie_graph(filename))
    
    def make_all_graphs(self):
        '''
            Generates all sample graphs and saves them.  
        '''
        self.make_bird_population_graph()
        self.make_population_graph()
        self.make_calorie_graph()