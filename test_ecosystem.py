import agressionSimulation as sim 
import matplotlib.pyplot as plt

sl = sim.simulation_logger()
eco = sim.ecosystem(sl)
eco.spawnBirds(100, 0.5, 100, 200, 10, 0.5)
eco.spawnForest(40, 50, 15, 25, 5, 3)
eco.time(days=365*3)
eco.save_results("testing_ecosystem_results")
eco.make_all_graphs()