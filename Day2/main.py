import csv
import re

## Calculate the sum of game ids that satisfy the constraints of 12 red, 13 green, 14 blue
def calculate_pt1(row):
    # Initialize the game id to 0
    gameid = 0
    
    # Initialize the color variables to 0
    r = g = b = 0
    
    # For each color in each part of the row, find the maximum number
    # and assign it to the corresponding color variable
    for value in row[1:]:
        parts = value.split(',')
        for part in parts:
            part = part.strip()  # remove leading and trailing spaces
            if 'red' in part:
                match = re.search(r'(\d+)\s*red', part)
                if match:
                    r = max(r, int(match.group(1))) # update red count
            if 'green' in part:
                match = re.search(r'(\d+)\s*green', part) 
                if match:
                    g = max(g, int(match.group(1))) # update green count
            if 'blue' in part:
                match = re.search(r'(\d+)\s*blue', part)
                if match:
                    b = max(b, int(match.group(1))) # update blue count
    print("Red:", r)
    print("Green:", g)
    print("Blue:", b)
    
    # Validate the counts against the game constraints
    if validate_constraints(r,g,b):
        # If it does, get the game id and store it so it can be returned to be added to sum of game ids
        gameid += int(re.search(r'\d+', row[0]).group())
        return gameid
        print(row[0]+" is within game constraints")
    else:
        print(row[0]+" is not within game constraints")
    #return gameid

## Validation that each game cube satisfy the constraints of 12 red, 13 green, 14 blue, if not return false.
def validate_constraints(r,g,b):
    within_constraints = True
    if r > 12:
        within_constraints = False
    if g > 13:
        within_constraints = False
    if b > 14:
        within_constraints = False
    return within_constraints

## Calculate power of set cubes 
def calculate_pt2(row):
    sumofpower = 0
    print(row)
    r = g = b = 0
    for value in row[1:]:
        parts = value.split(',')
        r_temp = g_temp = b_temp = 0
        for part in parts:
            part = part.strip()  # remove leading and trailing spaces
            if 'red' in part:
                match = re.search(r'(\d+)\s*red', part)
                if match:
                    r_temp = max(r_temp, int(match.group(1)))
            if 'green' in part:
                match = re.search(r'(\d+)\s*green', part)
                if match:
                    g_temp = max(g_temp, int(match.group(1)))
            if 'blue' in part:
                match = re.search(r'(\d+)\s*blue', part)
                if match:
                    b_temp = max(b_temp, int(match.group(1)))
        r = max(r, r_temp)
        g = max(g, g_temp)
        b = max(b, b_temp)
    print("Red:", r)
    print("Green:", g)
    print("Blue:", b)
    sumofpower += sum_of_power(r,g,b)
    return sumofpower

def sum_of_power(r,g,b):
    return r * g * b

csvfile2 = "C:\\Users\\Mohammed\\Documents\\VisualStudioCode\\AdventCode\\Day2\\adventday2.csv"

with open(csvfile2, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    sumofgameints = 0
    sumofgamepower = 0
    gameswithinconstraint = []
    for row in reader:
        if row:  # Check if row is not empty
            sumofints = calculate_pt1(row)
            sumofpower = calculate_pt2(row)
            sumofgamepower += sumofpower
            if sumofints:
                gameswithinconstraint.append(sumofints)
                sumofgameints += sumofints
            
    print()

    print("Game Ids within constraints:", gameswithinconstraint)
    print("Sum of IDs:", sumofgameints)
    print()
    print("Sum of game power:", sumofgamepower)
