from collections import deque, defaultdict


filename = "C:\\Users\\Mohammed\\Documents\\VisualStudioCode\\AdventCode\\Day4\\adventday4input.txt"

# This function takes in filename and splits the data into a list of lists where each list is a game. 
# Anything behind ':' is the game number, the second content is winning numbers and the third content is your numbers
# Winning numbers and your numbers are seperated by '|'

def load_data(filename):
    sum = 0
    with open(filename, 'r') as file:
        data = [[item.split('|') for item in line.strip().split(':')] for line in file]
        for row in data:
            #print(row[1])
            # Check if winning numbers are in your numbers
            for item in row[1]:
                x = 0
                if item in row[1][x]:
                    tmpsum = 1
                    row[1][0] = row[1][0].split()
                    row[1][1] = row[1][1].split()
                    matches = list(set(row[1][0]).intersection(row[1][1]))
                    if len(matches) >= 1:
                        for _ in range(len(matches)-1):
                            tmpsum *= 2
                        sum += tmpsum
    print(sum)
    
def process_cards(cards):
    i = 0
    while i < len(cards):
        #print(i)
        card = cards[i]
        instance = 0
        append_cards(cards)
        #print(card[2])
        matches = list(set(card[1][0]).intersection(card[1][1]))
        if len(matches) >= 1:
            #print(len(matches))
            print(len(matches)," matches in:", card[0])
            for x in range(len(matches)):
                cards[i+x][2] += 1
                print("match")
                #print("match added to card: ", cards[i+x][0])
            #print("match")
                #next_card = i + 1
                #if next_card < len(cards):
                #cards.append(cards[next_card])
        #print(cards[i][2])
        i += 1
    newint = work_cards(cards)
    return newint

def work_cards(cards):
    sum = 0
    for card in cards:
        sum += card[2]
    print(sum)

def append_cards(cards):
    for card in cards:
        card.append(1)
    return cards

def load_data2(filename):
    with open(filename, 'r') as file:
        data = [[item.split('|') for item in line.strip().split(':')] for line in file]
        for row in data:
            for item in row[1]:
                if item in row[1][0]:
                    row[1][0] = row[1][0].split()
                    row[1][1] = row[1][1].split()
    return data

cards = load_data2(filename)
print(process_cards(cards))