import agressionSimulation as sim

# # TODO: Testing the clearing function
# from birds import bird
# from simulation_logger import simulation_logger
# bird1 = bird()
# bird1.setBirdChars("H", "M", 100, 200, 10)
# bird2 = bird()
# bird2.setBirdChars('H', "F", 100, 200, 10)
# sl = simulation_logger()
# sl.new_day()
# sl.new_day()
# cl = clearing(100, 10, 1, simulation_logger=sl)

# # Testing the occupy feature 
# cl.occupy(bird1, bird2)
# print(f"cl calories: {cl.calories}")
# cl.growth()
# print(f'cl growth: {cl.calories}, bird1cal: {bird1.calories}, bird2cals: {bird2.calories}')
# cl.resolve()
# print(f'cl resolve: {cl.calories}, bird1cal: {bird1.calories}, bird2cals: {bird2.calories}')
# print(cl.time())
# print(f'cl time: {cl.calories}, bird1cal: {bird1.calories}, bird2cals: {bird2.calories}')
# sl.save()