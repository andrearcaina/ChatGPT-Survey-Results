import csv # library for reading data 

'''
    what this file does:
        - open Generalized Responses csv file 
        - read it and append it to a list of lists
        - get each respective question responses into list
        - write to a csv file (for clarity and readability) 
'''
def remove_spaces(data):
    return [i for i in data if i != '']

with open("./data/ChatGPT Generalized Responses.csv","r") as f:
    r = csv.reader(f,delimiter=",")
    RESPONSES = []
    for row in r:
        RESPONSES.append(row)

AGE           = remove_spaces([row[1] for row in RESPONSES])
DEPARTMENT    = remove_spaces([row[5] for row in RESPONSES])
HEARD         = remove_spaces([row[6] for row in RESPONSES])
USAGE         = remove_spaces([row[7] for row in RESPONSES])
IMPROVEMENT   = remove_spaces([row[8] for row in RESPONSES])
RELIABILITY   = remove_spaces([row[9] for row in RESPONSES])
LEARNING      = remove_spaces([row[10] for row in RESPONSES])
DISHONESTY    = remove_spaces([row[11] for row in RESPONSES])
ASSISTANCE    = remove_spaces([row[12] for row in RESPONSES])         

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

# this is not necessary (unless you want the spreadsheet or excel with the csv file)
with open("./data/Individual Data.csv","w",newline='') as f:
    write = csv.writer(f,delimiter=",")
    for data_row in IMPROVED_DATA:
        write.writerow(data_row)