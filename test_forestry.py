from agressionSimulation import bird, clearing, forest, simulation_logger

# Set up testing variables
bird1 = bird()
bird1.setBirdChars("H", "M", 100, 200, 10)
bird2 = bird()
bird2.setBirdChars('H', "F", 100, 200, 10)
sl = simulation_logger()
sl.new_day()

# Create forest object
fr = forest(2, 10, 1, 1, 0.1, 3, sl)

# Test the load function 
fr.load([bird1, bird2])
assert fr.allBirds == [bird1, bird2]
assert len(fr.spaces) == 2

# Test the occupy function
fr.occupy()
count_birds = len(fr.nonOccupiedBirds)
for cl in fr.spaces:
    count_birds += len(cl.birds)

# Test the time function via the simulation_logger save function 
fr = forest(2, 10, 1, 1, 0.1, 3, sl)
fr.load([bird1, bird2])
for day in range(0, 25):
    fr.time()

sl.save()
print("Passed all forestry tests!")