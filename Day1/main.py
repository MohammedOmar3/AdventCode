import csv
import re
from word2number import w2n

def load_data(filename):
    mylist = []
    with open(filename) as numbers:
        numbers_data = csv.reader(numbers)
    ##next(numbers_data)
        for row in numbers_data:
            mylist.append(row[0])
        return mylist

def get_digits(list):
    new_digits = []
    for row in list:
        txt = "".join(str(row))
        ##print (txt)
        new_dig = re.findall(r'\d+', txt)
        new_txt = "".join(new_dig)
        final = first_last_digit(new_txt)
        new_digits.append(final)
    return new_digits

def get_digits2(list):
    new_digits = []
    for row in list:
        txt = "".join(str(row))
        newtxt = w2n2(txt)
        new_dig = re.findall(r'\d+', newtxt)
        new_txt = "".join(new_dig)
        final = first_last_digit(new_txt)
        new_digits.append(final)
    return new_digits

def w2n2(number):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    number = (
        number.replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine")
        )
    for word in words:
        if word in number:
            start = number.index(word)
            end = start + len(word)
            print(f'Word "{word}" starts at {start} and ends at {end}')
            extracted_word = number[start:end]
            number = number.replace(word, str(words.index(extracted_word)) )
    return number

def first_last_digit(stringtext):
    together = ""
    if len(stringtext) > 1:
        firstdigit = str(stringtext)[-1]
        lastdigit = str(stringtext)[0]
        together = lastdigit + firstdigit
    else: 
        firstdigit = str(stringtext)[-1]
        lastdigit = str(stringtext)[0]
        together = lastdigit + firstdigit
    return together

def totalint(list):
    totali = 0
    for row in list:
        totali += int(row)
    return totali

new_list = load_data('C:\\Users\\Mohammed\\Desktop\\project_starter_\\adventcode\\adventday1.csv')
##for row in new_list:
    ##print(row)
my_number = len(new_list)
##print(my_number)
print("done")
print(new_list)
new_digits = get_digits2(new_list)
print(new_digits)
for row in new_digits:
   print(row)
totalin = totalint(new_digits)
print(totalin)
