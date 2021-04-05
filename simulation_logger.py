try:
    import pandas as pd
except:
    raise ImportError("Unable to import required modules. Please install the requirements.txt file.")

class simulation_logger():
    def __init__(self):
        self.df_columns = ["day", "num_of_doves", "num_of_hawks", "population", 
                                            "dove_births", "dove_deaths", "hawk_births", "hawk_deaths"]
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
        # Increment the values recoreded within the csv 

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

    def show(self, day=None):
        # Show the status of the current simulation

        # If day is specificed, print that day
        if day is not None:
            try:
                print(self.df.loc[day])
            except:
                print(f"day {day} does not exist within the simulation")
        
        # else, show the first 5 entries 
        else:
            print(self.df.head())
        
        return 0
    
    def save(self, filename="simulation_results"):
        # Save the csv to the results folder, with a supplied filename

        self.df.to_csv(f"results//{filename.strip()}.csv")

