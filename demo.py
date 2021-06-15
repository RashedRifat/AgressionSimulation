import agressionSimulation as sim 
import matplotlib.pyplot as plt

sl = sim.simulation_logger()
eco = sim.ecosystem(sl)
eco.spawnBirds(1000, 0.5, 100, 200, 10, 0.5)
eco.spawnForest(400, 50, 15, 25, 5, 3)
eco.time(days=365*10)
eco.save_results("simulation_results")
eco.make_all_graphs()