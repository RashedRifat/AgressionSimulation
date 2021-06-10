import agressionSimulation as sim 

sl = sim.simulation_logger()
eco = sim.ecosystem(sl)
eco.spawnBirds(100, 0.5, 100, 200, 10, 0.5)
eco.spawnForest(100, 35, 15, 15, 5, 3)
print(eco.numOfDoves(), eco.numOfHawks(), eco.totalPopulation())
eco.time(days=100)
eco.save_results("testing_ecosystem_results")