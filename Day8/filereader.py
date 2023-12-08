import csv
from itertools import islice

def txt_to_csv(txt_filename, csv_filename, start_line=3):
    with open(txt_filename, 'r') as txt_file, open(csv_filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for line in islice(txt_file, start_line - 1, None):
            # Split the line into columns
            columns = line.split('=')
            # Further split the second column into two columns
            columns[1:] = columns[1].strip().split(',')
            # Remove parentheses from the second and third columns
            columns[1:] = [col.replace('(', '').replace(')', '') for col in columns[1:]]
            # Write the columns to the CSV file
            writer.writerow(columns)

def first_line_to_list(filename):
    with open(filename, 'r') as file:
        first_line = file.readline()
    return list(first_line.strip())

def remove_spaces(csv_filename):
    # Read the data
    with open(csv_filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        data = list(reader)

    # Remove spaces
    data = [[item.replace(' ', '') for item in row] for row in data]

    # Write the data back to the file
    with open(csv_filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)

csv_filename = "C:\\Users\\Mohammed\\Documents\\VisualStudioCode\\AdventCode\\Day8\\adventday8output.csv"
remove_spaces(csv_filename)
    
def main():
    txt_to_csv("C:\\Users\\Mohammed\\Documents\\VisualStudioCode\\AdventCode\\Day8\\adventday8input.txt", "C:\\Users\\Mohammed\\Documents\\VisualStudioCode\\AdventCode\\Day8\\adventday8input.csv")