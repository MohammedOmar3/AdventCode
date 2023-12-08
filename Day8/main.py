'''
This program solves the problem for Day 8 of the Advent of Code 2019.
The problem is described at https://adventofcode.com/2019/day/8

The program reads the input file, converts it to a CSV file, and then navigates
the network based on the left/right instructions. The program then prints the
number of steps required to reach the exit.

The program also navigates the network in part 2 of the problem, and prints the
number of steps required to reach the exit.
'''
from filereader import first_line_to_list, main
import csv
from math import lcm

# Convert the input file to a CSV file
def csv_to_list(csv_filename):
    with open(csv_filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        data_list = list(reader)
    return data_list

# Function to navigate a network based on a list of directions
def navigate_network(location, directions):
    # Initialize start and end nodes
    startnode = 0
    endnode = 0

    # Find the indices of the start and end nodes in the location list
    while startnode == 0 & endnode == 0:
        for x, loc in enumerate(location):
            if loc[0] == 'AAA':  # If the first element of the location is 'AAA', set it as the start node
                startnode = x
            if loc[0] == 'ZZZ':  # If the first element of the location is 'ZZZ', set it as the end node
                endnode = x

    # Start navigation from the start node
    currentnode = startnode
    steps = 0  # Initialize step counter
    reached = False  # Initialize flag to check if end node is reached

    # Navigate the network until the end node is reached
    while reached == False:
        for direction in directions:
            # Update the current node based on the direction
            currentnode = location[currentnode][1 if direction == 'L' else 2]
            steps += 1  # Increment step counter

            # Check if the end node is reached
            if currentnode == 'ZZZ':
                reached = True  # Set the flag to True to exit the loop
                break
            else:
                # If the end node is not reached, update the current node index
                currentnode = getindex(location, currentnode)

    # Return the number of steps taken to reach the end node
    return steps

# Function to navigate a network based on a list of directions
def navigate_networkpt2(location, directions):
    # Initialize start and end nodes as empty lists
    startnode = []
    endnode = []

    # Find the indices of the start and end nodes in the location list
    for x, loc in enumerate(location):
        if loc[0].endswith('A'):  # If the first element of the location ends with 'A', add it to the start nodes
            startnode.append(x)
        if loc[0].endswith('Z'):  # If the first element of the location ends with 'Z', add it to the end nodes
            endnode.append(x)

    # Initialize step counter
    steps = 0

    # Start navigation from the start nodes
    currentnode = startnode

    # Initialize the number of nodes reached
    reached = len(currentnode)

    # Initialize list to store the number of steps taken to reach each end node
    finished = []

    # Navigate the network until all end nodes are reached
    while len(currentnode) != 0:
        x = 0
        for direction in directions:
            # Update the current node based on the direction
            currentnode[x] = location[currentnode[x]][1 if direction == 'L' else 2]
            steps += 1  # Increment step counter

            # Update the current node index
            currentnode[x] = getindex(location, currentnode[x])

            # Check if the current node is an end node
            if currentnode[x] in endnode:
                finished.append(steps)  # Add the number of steps taken to the finished list
                endnode.remove(currentnode[x])  # Remove the current node from the end nodes
                currentnode.remove(currentnode[x])  # Remove the current node from the current nodes
                x += 1  # Move to the next node
                reached -= 1  # Decrement the number of nodes reached
                steps = 0  # Reset the step counter

    # Calculate the least common multiple of the number of steps taken to reach each end node
    steps = lcm(*finished)

    # Return the number of steps taken to reach all end nodes
    return steps

# Function to get the index of a node in the location list
def getindex(location, name):
    for x, loc in enumerate(location):
        if loc[0] == name:
            return x
    return -1

# Main function
def main():
    # Read the first line of the input file into list: This is the directions.
    li = first_line_to_list("C:\\Users\\Mohammed\\Documents\\VisualStudioCode\\AdventCode\\Day8\\adventday8input.txt")
    
    # Read the CSV file into a list
    csv_filename = "C:\\Users\\Mohammed\\Documents\\VisualStudioCode\\AdventCode\\Day8\\adventday8output.csv"
    data_list = csv_to_list(csv_filename)
    
    # Navigate the networks
    pt1steps = navigate_network(data_list, li)
    pt2steps = navigate_networkpt2(data_list, li)
    
    # Print the result
    print(f'The packet requires {pt1steps} steps to reach the exit.')
    print(f'The packet requires {pt2steps} steps to reach the exit.')

if __name__ == "__main__":
    main() # Run the main function