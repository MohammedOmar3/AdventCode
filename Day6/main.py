'''
# Toy boat race simulation
# Each boat has a button that when held down charges the boat
# The longer the button is held, the faster the boat moves
# Time spent holding the button counts against total race time
# The button can only be held at the start of the race
# Boats don't move until the button is released

# The speed of the boat increases by 1mm/ms for each ms the button is held down
# The goal is to determine the number of ways to beat the record in each race
# This is done by calculating the number of different times the button can be held down
# such that the resulting distance is greater than the record distance

Test Race:
Time:      7  15   30
Distance:  9  40  200

Race part 1:
Time:        44     89     96     91
Distance:   277   1136   1890   1768

# Part Two modifies the problem by merging all the races into a single long race
# The goal remains the same: determine the number of ways to beat the record

Race Part 2:
Time:       44899691
Distance:   277113618901768
'''

test_races = [[7, 9],[15, 40],[30, 200]]
racespart1 = [[44,277],[89,1136],[96,1890],[91,1768]]
racespart2 = [[44899691,277113618901768]]

# Define a function to calculate the number of ways to win each race
def sum(races):
    # Initialize a list to store the number of ways to win each race
    record = []
    # Iterate over each race
    for race in races:
        # Initialize a list to store the number of ways to win the current race
        waystowin = []
        # Extract the race time and record distance from the race list
        recordtime = race[0]
        distancetobeat = race[1]
        # Initialize the distance travelled by the boat to 0
        distance = 0
        # Iterate over each possible button hold time from 0 to the race time
        for x in range(race[0]+1):
            # Set the button hold time to the current iteration value
            button = x
            # If the button hold time is less than or equal to the race time
            if x <= recordtime:
                # Calculate the remaining time after the button is released
                timeleft = recordtime - x
                # Calculate the distance travelled by the boat
                distance = (button*timeleft)
            
            # If the distance travelled by the boat is greater than the record distance
            if distance>distancetobeat:
                waystowin.append(x)
        #print(waystowin)
        record.append(len(waystowin))
    print(record)
  
sum(racespart1)
sum(racespart2)