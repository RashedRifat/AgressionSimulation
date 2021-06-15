try:
    import pandas as pd
    import matplotlib.pyplot as plt
except ImportError as ex:
    raise ImportError("Unable to import required modules. Please install the requirements.txt file.\n" + ex.with_traceback())

class simulation_logger():
    def __init__(self):
        self.df_columns = ["day", "num_of_doves", "num_of_hawks", "population", 
                            "dove_births", "dove_deaths", "hawk_births", "hawk_deaths", "total_calories",
                            "calories_after_feeding"]
        self.df = pd.DataFrame(columns=self.df_columns)
        self.day_counter = -1
        
    def new_day(self):
        # Intialize a new row in the dataframe

        self.day_counter += 1
        self.df.loc[self.day_counter, "day"] = self.day_counter

        for elem in self.df_columns[1:]:
            self.df.loc[self.day_counter, elem] = 0
    
    def increment(self, num_of_doves=None, num_of_hawks=None, 
                        dove_births=None, dove_deaths=None, hawk_births=None, hawk_deaths=None):
       
        # Increment the values recoreded within the database 
        if num_of_doves is not None:
            self.df.loc[self.day_counter, "num_of_doves"] += num_of_doves
            self.df.loc[self.day_counter, "population"] += num_of_doves

        if num_of_hawks is not None:
            self.df.loc[self.day_counter, "num_of_hawks"] += num_of_hawks
            self.df.loc[self.day_counter, "population"] += num_of_hawks
        
        if dove_births is not None:
            self.df.loc[self.day_counter, "dove_births"] += dove_births

        if dove_deaths is not None:
            self.df.loc[self.day_counter, "dove_deaths"] += dove_deaths
        
        if hawk_births is not None:
            self.df.loc[self.day_counter, "hawk_births"] += hawk_births
        
        if hawk_deaths is not None:
            self.df.loc[self.day_counter, "hawk_deaths"] += hawk_deaths

    def show(self, n=5):
        # Show a preview of the results 
        print(self.df.head(n=n))

    def add(self, bird, child=False):
        # Increment a bird based on its charactersitics 

        # Handle if bird is alive 
        if bird.alive:

            # Handle if bird is dove or haw
            if bird.isDove():
                self.increment(num_of_doves=1)

                # If the bird is a child, increment approiately 
                if child:
                    self.increment(dove_births=1)
            else:
                self.increment(num_of_hawks=1)
                if child:
                    self.increment(hawk_births=1)
                    
        # If the bird is dead, add to the death counter 
        else:
            if bird.isDove():
                self.increment(dove_deaths=1)
            else:
                self.increment(hawk_deaths=1)        
                

    def add_space(self, data):
        # Add the calories of a space 
        col1 = "total_calories"
        col2 = "calories_after_feeding"

        self.df.loc[self.day_counter, col1] += round(data[0], 2)
        self.df.loc[self.day_counter, col2] += round(data[1], 2)
    
    def save(self, filename="simulation_results"):

        # Save the csv to the results folder, with a supplied filename
        self.df.to_csv(f"results//{filename.strip()}.csv")
    
    def make_population_graph(self, filename=""):
        plt.plot(range(0, self.df.shape[0]), self.df["population"])
        plt.title("Population of Birds Over Time")
        plt.xlabel("Days")
        plt.ylabel("Bird Population")
        
        # Save the grpah 
        if filename:
            filename = f"results//{filename}.png"
        else:
            filename = "results//population_grapgh.png"
        
        plt.show()
        plt.savefig(filename)
        return f"Plot saved to {filename}"
    
    def make_bird_population_graph(self, filename=""):
        plt.plot(range(0, self.df.shape[0]), self.df[["num_of_doves", "num_of_hawks"]])
        plt.title("Population of Doves and Birds Over Time")
        plt.xlabel("Days")
        plt.ylabel("Number of Birds")
        plt.legend(["Doves", "Hawks"])

        # Save the grpah 
        if filename:
            filename = f"results//{filename}.png"
        else:
            filename = "results//bird_population_grapgh.png"
        
        plt.show()
        plt.savefig(filename)
        return f"Plot saved to {filename}"
    
    def make_calorie_graph(self, filename=""):
        plt.plot(range(0, self.df.shape[0]), self.df[["total_calories", "calories_after_feeding"]])
        plt.title("Calories Over Time")
        plt.xlabel("Days")
        plt.ylabel("Calories")
        plt.legend(["Total Calories", "Calories After Feeding"])

        # Save the grpah 
        if filename:
            filename = f"results//{filename}.png"
        else:
            filename = "results//calorie_graph.png"

        plt.savefig(filename)
        plt.show()
        return f"Plot saved to {filename}"
