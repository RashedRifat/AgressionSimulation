import agressionSimulation as sim

# Testing bird creation 
bird1 = sim.bird()
bird1.setBirdChars("H", "M", 100, 200, 10)
bird2 = sim.bird()
bird2.setBirdChars('H', "F", 100, 200, 10)

# Check basic setters
assert bird1.isHawk() == True
assert bird1.isDove() == False
assert bird1.isMale() == True
assert bird2.isMale() == False
assert bird1.isFemale() == False
assert bird2.isFemale() == True

# Check addCalories function
    # Try passing in incoorect type for addCalories
try:
    bird1.addCalories(None)
    raise AssertionError("Failed adding None calories to bird")
except ValueError as ex:
    pass 

    # Try passing in incoorect TYpe for addCalories 
try:
    bird1.addCalories(-1)
    raise AssertionError("Failed adding negative calories to bird")
except ValueError as ex:
    pass

    # Pass in proper values and check for caloric limit cdcd
bird1.addCalories(100)
assert bird1.calories == 200
bird1.addCalories(100)
assert bird1.calories == 200

# Check agression function
    # Try passing in incorrect types 
    # TODO: redo these tests 
try:
    bird1.aggresion(1, 1)
    raise AssertionError("Failed agression function with incorrect bird type")
except TypeError as ex:
    pass

    # Try passing in None calories
try:
    bird1.aggresion(bird2, None)
    raise AssertionError("Failed agression function with None calories")
except ValueError as ex:
    pass

    # Try passing in negative calories 
try:
    bird1.aggresion(bird2, -1)
    raise AssertionError("Failed agression function with negative calories")
except ValueError as ex:
    pass

    # Try passing in correct values 
bird1.calories = 100
bird1.aggresion(bird2, 100)
assert bird1.calories + bird2.calories == 300

bird1.calories = 100
bird1.aggresion(None, 100)
assert bird1.calories == 200

# Check procreate function 
    # Try passing in incorrect types 
try:
    bird1.procreate(1)
    raise AssertionError("Failed procreate function with incorrect bird type")
except TypeError as ex:
    pass

    # Try passing in a dead pird 
bird3 = sim.bird()
bird3.alive == False
assert bird1.procreate(bird3) == []

    # Try passing in a bird of the same gender
bird3.alive = True
bird3.gender = bird1.gender
assert bird1.procreate(bird3) == []

    # Try passing in a bird of a different species 
bird3.gender = 'F'
bird3.species = "D"
assert bird1.procreate(bird1) == []

    # Try passing in a bird with all the correct characteristics 
assert len(bird1.procreate(bird2)) == 1
assert bird1.procreate(None) == []


print("All bird tests passed successfully!")