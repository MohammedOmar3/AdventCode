import csv
txtfile = "C:\\Users\\Mohammed\\Documents\\VisualStudioCode\\AdventCode\\Day3\\adventday3input.txt"
csvfile = "C:\\Users\\Mohammed\\Documents\\VisualStudioCode\\AdventCode\\Day2\\adventday3.csv"

d = {}
with open(txtfile) as f:
    for line in f:
       (key, val) = line.split()
       d[int(key)] = val