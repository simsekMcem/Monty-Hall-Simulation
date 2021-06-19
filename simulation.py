import random
import sys

"""
Problem definition in real life:

Suppose you're on a game show, and you're given the choice of three doors:
Behind one door is a car; behind the others, goats.
You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat.
He then says to you, "Do you want to pick door No. 2?"

Is it to your advantage to switch your choice?
"""


# variables
goat = 0 
car = 1

# functions
def blindGuessChance(numberOfDoors):
    return 100 * float(1)/numberOfDoors

def removeRandomGoat(doors):
    randomChoice = random.randint(0, len(doors)-1)
    if(doors[randomChoice] == 0):
        del doors[randomChoice] # Not efficient but it is certain that we remove one goat
        return doors
    else:
        return removeRandomGoat(doors)

def initDoors(numberOfDoors):
    doors = []
    for i in range(0, numberOfDoors-1):
        doors.append(goat) # add goats behind the doors
    doors.append(car) # add only one car
    #random.shuffle(doors) # Make sure that index of the car is unknown -- This is unnecessary since we choose random doors
    return doors

def runSimulation(numberOfDoors):
    doors = initDoors(numberOfDoors)
    choice = random.randint(0, numberOfDoors-1) # choose random door (array index)
    doors[choice] = "Selected"
    
    while len(doors) != 2: # remove goats until there are two door options
        removeRandomGoat(doors)
    
    # At this moment, if the first guess is correct,
    # Then doors would be [0, "selected"]
    # Otherwise, doors would be [1, "selected"]
    # The non-string element is the choice if we switch
    if 0 in doors:
        return "goat"
    else:
        return "car"

def simulations(numberOfDoors, simulationNumber):
    car = 0
    goat = 0
    for i in range(0, simulationNumber):
        rewardWhenSwitch = runSimulation(numberOfDoors)
        if rewardWhenSwitch == "car":
            car = car + 1
        else:
            goat = goat + 1
    
    print("There has been " + str(simulationNumber) + " simulations with " + str(numberOfDoors) + "doors.")
    print("The probability of winning the car with blind guess is %" + str(blindGuessChance(numberOfDoors)) + ".")
    print("If you would have switched your choice, you would win " + str(car) + " cars and win " + str(goat) + " goats.")
    print("Probability of winning if you switch is %" + str(100 * (float(car)/simulationNumber)) + ".")

numberOfDoors, simulationNumber = int(sys.argv[1]), int(sys.argv[2])
simulations(numberOfDoors, simulationNumber)