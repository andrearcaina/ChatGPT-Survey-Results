import csv                          # library for reading data 

'''
    what this file does:
        - open Generalized Responses csv file 
        - read it and append it to a list of lists
        - get each respective question responses into list
        - write to a csv file (for clarity and readability) 
'''

with open("./data/ChatGPT Generalized Responses.csv","r") as f:
    r = csv.reader(f,delimiter=",")
    RESPONSES = []
    for row in r:
        RESPONSES.append(row)

AGE           = [row[1] for row in RESPONSES]
DEPARTMENT    = [row[5] for row in RESPONSES]
HEARD         = [row[6] for row in RESPONSES]
USAGE         = [row[7] for row in RESPONSES]
IMPROVEMENT   = [row[8] for row in RESPONSES]
RELIABILITY   = [row[9] for row in RESPONSES]
LEARNING      = [row[10] for row in RESPONSES]
DISHONESTY    = [row[11] for row in RESPONSES]
ASSISTANCE    = [row[12] for row in RESPONSES]             

IMPROVED_DATA = [
                    AGE,
                    DEPARTMENT,
                    HEARD,
                    USAGE,
                    IMPROVEMENT,
                    RELIABILITY,
                    LEARNING,
                    DISHONESTY,
                    ASSISTANCE
                ]

with open("./data/Individual Data.csv","w",newline='') as f:
    write = csv.writer(f,delimiter=",")
    for data_row in IMPROVED_DATA:
        write.writerow(data_row)