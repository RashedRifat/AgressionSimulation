# Import in the simulation package 
import agressionSimulation as sim 

# Create a simulation logger and the ecosystem in which this simulation will be run 
sl = sim.simulation_logger()
eco = sim.ecosystem(sl)

# Spawn the birds and the forest within the simulation 
eco.spawnBirds(1000, 0.5, 100, 200, 10, 0.5)
eco.spawnForest(400, 50, 15, 25, 5, 3)

# Simulate the passing of time within the forest, saving the results and plots to the results directory 
eco.time(days=365*10)
eco.save_results("simulation_results")
eco.make_all_graphs()