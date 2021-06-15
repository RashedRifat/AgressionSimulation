# AgressionSimulation

The prupose of this project was to simulate how aggression would affect survival in gathering sufficent food in the wild. This was accomplished by creating two populations of birds, doves and hawks, which would compete in a forest for food and survival. Doves were treated to less agressive and would share food upon discovering it, whereas hawks would always fight for the larger portion. This competition for survival took place in a forest, where food was distributed randomly through the clearings in the forest (spaces where birds would meet to either share or fight for food) and also grew back at a normally distributed rate. All of these parameters can be specificed within the simulation. Examples are noted below.  

## The Narrative 
During each day of the simulation, birds would attempt to gather food within the forest, which was spawned with a specified amount of spaces and calories. A bird can attempt to find a non-occupied clearing a set amount of times before retiring from the hunt. A non-occupied clearing is one in which there are less than two birds (regardless of species). Within a clearing, doves share food equally whereas hawks would fight for their food. If a dove and a hawk met, then the dove runs away, leaving the larger portion of the food to the hawk. If two birds of the same species and opposing genders meet within the same clearing, then they produce an offspring of the same species and a random gender. At the end of the day, a set number of calories is extracted from each bird, taken to be the daily cost of survival. The clearings within the forest will also regenerate some of the food consumed during the day at this time. The next day, the cycle repeats and the results are logged for your persual. 

To measure the results of the simulation, several graphs were plotted, such as the overall bird population over time, population of doves vs hawks over time and the caloric value of the forest over time. Some preliminary analysis showed that over tiem, hawks were shown to survive for longer periods of time with a much larger population than either their intial starting population or the dove population. 

Some notable effects such as the carrying capacity of an environment naturally arose from the simulation. This can be observed from the stablization of both the dove and bird populations at some level determined by the avaliability of calories within the forest (and the simulation), such as the total space of the forest and the rate at which the forest grew back it's calories. 

It must be noted that this is a low-level simulation with many factors abstracted out for the sake of simplicity. Use of this simulation should be done with these factors in mind. Some results are shown below. 

## Selected Results 
Intial Testing Conditions:
1. Total Stating Population: 1000 birds  
2. Chance of Spawning a Dove: 50%
3. Chance of Spaawning a Hawk: 50%
4. Birds started with 100 calories 
5. Birds had a maximum caloric limit of 200 calories 
6. Birds spent 10 caloires per day 
7. There was an even split between males and females spawning for each population. 
8. A forest with 400 spaces was spawned 
9. On average, the starting calories for the spaces within the forest was distributed normally with a mean of 50 calories and a standard deviation of 15 calories. 
10. On average, the forest regrew with a mean of 25 calories and a standard deviation of 5 calories per clearing 
11. Each bird had a maximum of 3 tries to find a non-occupied clearing to either share or fight for food before they gave up for the day. 
12. This simulation was ran for 10 years (365 * 10 days). 

This simulation took approximately 22 minutes to complete. The results of the simulation was saved in a CSV within the results folder. Selected graphs of the results are shown below. 

![Population Over Time](/results/population_graph.png) <br/>
![Bird Population Over Time](/results/bird_population_graph.png) <br/>
![Calories Over Time](/results/calorie_graph.png)

## Intial Setup 

To run this simulation for yourself, download this repo and install the requirements via the requirements.txt file. Refer to the demo for an example of what this simulation can do and the results it produces. Specific documentation on each class and function is noted below and within the code. 

## A Deeper Dive 

Here we examine some of the classes and objects created for this simulation. Each method has its appropriate documentation within the implementation of each class. 

### Birds 

This class represents a bird within the simulation. A bird has a specific ID, species, gender, calories, a calorie limit, daily expenditure needed to stay alive and a set number of starting calories. 

Each day a bird attempts to gather food from the forest, within spaces called clearings. A bird can attempt to gather food a limited number of times before it retires and goes hungry for the night. If a bird can occupy a clearing individually, it can gather some portion of the calories within the clearing. If two birds occupy the same clearing, then, depending on their species, they either share or fight for their food. 

Within a clearing, doves share food equally whereas hawks would fight for their food. If a dove and a hawk met, then the dove runs away, leaving the larger portion of the food to the hawk. If two birds of the same species and opposing genders meet within the same clearing, then they produce an offspring of the same species and a random gender. 

At the end of the day, a set number of calories is expended by all birds to attempt to stay alive. 

### Clearings 

A clearing is a space within the forest in which food can be gathered. For all intents and purposes, the total number of clearings within a forest denotes the size of the forest. 

A clearing spawns with a random number of calories within the forest, drawn from a normally distributed plot of calories. 

A clearing can host a total of at most two birds, regardless of species and gender. A portion of the avaliable calories within a clearing can be gathered by its occupants, which is further divided across its occupants based on their behaviour. A clearing is also the location in which a new bird can be spawned if two parents of the opposing gender and same species occupy the same space. The new bird will automatically join the race for food the next day.  

At the end of the day, the clearing regenerates some of the calories avaliable to it (simulating the growth of trees and small animals within a forest), as set by a normal distribution specifed with a mean and standard deviation. 

### Forests 

A forest represents one type of environemnt in which a simulation can take place. A forest contains some number of spaces, known as clearings, that effectively measure the total size of the forest. 

### Ecosystem

An ecosystem contains all of the birds and environments the simulation can have. Birds consist of doves and hawks while environments currently consist of only forests. In the future, other possible environments may be added. 

### SimulationLogger

A simulation logger is an object used to record the data for the simulation. This logger object logs the following data points per day:

- days: the current day within the simulation 
- num_of_doves: the population of doves for a day
- num_of_hawks: the population of hawks for a day
- population: the total bird population for a day 
- dove_births: the population of new doves spawned for a day 
- dove_deaths: the population of doves that died for a day 
- hawk_births: the population of new hawks spawned for a day
- hawk_deaths: the population of hawsk that died for a day 
- total_calories: the total number of avaliable calories within the forest for a day
- calories_after_feeding: the number of calories avaliable after the bird population has fed for the day 

Several base graphs can be generated from the data using the simulation logger, such as total population over time, populations of hawks vs doves over time and total calories over time. 

These results are stored within the results folder. 
