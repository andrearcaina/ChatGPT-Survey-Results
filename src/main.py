import matplotlib.pyplot as plt     # library for graphing data
import numpy as np                  # library for entering data

responses = np.genfromtxt("./data/ChatGPT Generalized Responses.csv",delimiter=',')

print(responses)                    # doesn't work. our data is flawed

'''
    what to do:
        - determine what graphs to present
        - then use the csv and the data to present it using matplotlib
'''