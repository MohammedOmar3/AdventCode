'''
Txt file that contains a puzzle input of a list of numbers with symbols. Any number adjacent to a symbol 
is a part number and should be included in the sum. Periods(.) do not count as a symbol.

The puzzle input is not seperated by commas or spaces. Each line can have multiple numbers of various digits. 
The numbers are seperated by symbols including period but in which this case periods does not count as a symbol.
'''

filename = "C:\\Users\\Mohammed\\Documents\\VisualStudioCode\\AdventCode\\Day3\\adventday3input.txt"

# This function takes in a filename and returns the sum of all numbers adjacent to symbols
def sum_numbers_adjacent_to_symbols(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file]

    # Get the number of rows and columns in the grid
    rows, cols = len(grid), len(grid[0])
    
    # Right, Left, Down, Up, DownRight, UpLeft, DownLeft, UpRight
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    total_sum = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j].isdigit():
                # If the current cell is part of a larger number, skip it
                if (j > 0 and grid[i][j-1].isdigit()) or (i > 0 and grid[i-1][j].isdigit()):
                    continue
                # Find the full number that the current cell is part of
                number = grid[i][j]
                k = j + 1
                while k < cols and grid[i][k].isdigit():
                    # Add the digit to the number
                    number += grid[i][k]
                    k += 1
                # Check if any digit of the number has a symbol in its neighboring cells
                has_symbol = False
                for l in range(j, k):
                    for dx, dy in directions:
                        nx, ny = i + dx, l + dy
                        # If the adjacent cell is a symbol, add the number to the total sum
                        if 0 <= nx < rows and 0 <= ny < cols and not grid[nx][ny].isdigit() and grid[nx][ny] != '.':
                            has_symbol = True
                            break
                    if has_symbol:
                        break
                if has_symbol:
                    # Add the number to the total sum
                    total_sum += int(number)

    return total_sum

def sum_gear_ratios(filename):
    # Read the grid from the input file
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file]

    # Get the number of rows and columns in the grid
    rows, cols = len(grid), len(grid[0])
                # Right, Left, Down, Up, DownRight, UpLeft, DownLeft, UpRight
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]  # Added diagonal directions

    total_sum = 0
    # Iterate over the grid
    for i in range(rows):
        for j in range(cols):
            # If the current cell is a symbol, check if it has two numbers adjacent to it
            if grid[i][j] == '*':
                numbers = []
                # Check if the current cell has two numbers adjacent to it
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    # If the adjacent cell is a number, add it to the list
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny].isdigit():
                        # Find the start of the number
                        start_y = ny
                        while 0 <= start_y - 1 < cols and grid[nx][start_y - 1].isdigit():
                            start_y -= 1
                        # Construct the number
                        number = ''
                        while 0 <= start_y < cols and grid[nx][start_y].isdigit():
                            number += grid[nx][start_y]
                            start_y += 1
                        numbers.append(int(number))
                # Removes duplicates for unique numbers
                unique_numbers = list(set(numbers))
                # If there are two unique numbers, add their product to the total sum
                if len(unique_numbers) >= 2:
                    total_sum += unique_numbers[0] * unique_numbers[1]
    return total_sum

print("Sum of numbers adjacent to symbols: ",sum_numbers_adjacent_to_symbols(filename))
print("Sum of gear ratios: ",sum_gear_ratios(filename))