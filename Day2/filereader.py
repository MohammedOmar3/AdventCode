import csv
txtfile = "C:\\Users\\Mohammed\\Documents\\AdventCode\\Day2\\adventday1input.txt"
csvfile = "C:\\Users\\Mohammed\\Documents\\AdventCode\\Day2\\adventday2.csv"

with open(txtfile, 'r') as infile, open(csvfile, 'w') as outfile:
    stripped = (line.strip() for line in infile)
    lines = ([line.split(':', 1)[0]] + line.split(':', 1)[1].split(';') for line in stripped if line)
    writer = csv.writer(outfile)
    writer.writerows(lines)