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
    # Try passing in None objects 
try:
    cl.occupy(None, bird1)
    raise AssertionError("Failed occupy function with none bird1 object")
except TypeError:
    pass

    # Try passing in incorrect type
try:
    cl.occupy(1, bird1)
    raise AssertionError("Failed occupy function with incorrect type bird1 object")
except TypeError:
    pass

try:
    cl.occupy(bird1, 1)
    raise AssertionError("Failed occupy function with incorrect type bird1 object")
except TypeError:
    pass

# Passing in the correct values 
cl.occupy(bird1, None)
assert cl.birds[0] == bird1 and cl.birds[1] == None

cl.occupy(bird1, bird2)
assert len(cl.birds) == 2

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


# TODO: Testing the forest class 
# Testing the load function 

# Testing the occupy function 

# Testing the time function 


# cl.occupy(bird1, bird2)
# print(f"cl calories: {cl.calories}")
# cl.growth()
# print(f'cl growth: {cl.calories}, bird1cal: {bird1.calories}, bird2cals: {bird2.calories}')
# cl.resolve()
# print(f'cl resolve: {cl.calories}, bird1cal: {bird1.calories}, bird2cals: {bird2.calories}')
# print(cl.time())
# print(f'cl time: {cl.calories}, bird1cal: {bird1.calories}, bird2cals: {bird2.calories}')
# sl.save()