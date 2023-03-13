from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # for drawing graphs on tkinter
import matplotlib.pyplot as plt                                 # library for graphing data
import numpy as np                                              # library for entering data

'''
    what to do:
        - determine what graphs to present
        - then use the csv and the data to present it using matplotlib
    
    what this code does:
        - use data from read_csv file and output the respective graphs
'''

# just prints it for now
def create_pie(data,title):
    print(title)
    values, totals = np.unique(data, return_counts=True)
    print(values, totals)

# just prints it for now
def create_bar(data,title): 
    print(title)
    values, totals = np.unique(data, return_counts=True)
    print(values, totals)