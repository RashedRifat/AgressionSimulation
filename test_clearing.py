from random import expovariate
from agressionSimulation import bird, clearing, forest, simulation_logger

# Generate testing objects 
bird1 = bird()
bird1.setBirdChars("H", "M", 100, 200, 10)
bird2 = bird()
bird2.setBirdChars('H', "F", 100, 200, 10)
sl = simulation_logger()
sl.new_day()
cl = clearing(100, 10, 1, simulation_logger=sl)

# TODO: Testing the clearing class
# Testing the occupy function 
try:
    cl.occupy(None)
except TypeError as ex:
    pass

try:
    cl.occupy("1")
except TypeError as ex:
    pass

cl.occupy(bird1)
cl.occupy(bird2)

try:
    cl.occupy(bird1)
except ValueError as ex:
    pass

# Testing the growth function 
oldClearingCals = cl.calories
cl.growth()
assert oldClearingCals < cl.calories

# Testing the resolve function 
oldClearingCals = cl.calories
oldBirdCals = [bird1.calories, bird2.calories]
assert len(cl.resolve()) == 1
assert oldClearingCals > cl.calories
assert bird1.calories > oldBirdCals[0]
assert bird2.calories > oldBirdCals[1]

print("Passed all clearing tests")