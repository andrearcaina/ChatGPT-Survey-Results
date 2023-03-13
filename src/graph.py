from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # for drawing graphs on tkinter
import matplotlib.pyplot as plt                                 # library for graphing data
import numpy as np                                              # library for entering data
from tkinter import Button

'''
    what to do:
        - determine what graphs to present
        - then use the csv and the data to present it using matplotlib
    
    what this code does:
        - use data from read_csv file and output the respective graphs
'''
def remove_figures(canvas,button):
    canvas.get_tk_widget().destroy()
    button.destroy()

def percentage(pct, allvals):
    absolute = int(np.round(pct / 100. * np.sum(allvals)))
    return "{:.1f}%".format(pct, absolute)

# just prints it for now
def create_pie(frame,data,title):
    values, totals = np.unique(data, return_counts=True)
    
    font = {'family' : 'Georgia',
            'weight' : 'normal',
            'size'   : 11
           }

    plt.rc('font', **font)

    fig, ax = plt.subplots(figsize=(5,5))

    fig.set_facecolor('#5A5A5A')
    ax.set_title(title, loc='center', wrap=True, color="w")
    ax.pie(
        totals, 
        radius=1,
        autopct= lambda pct: percentage(pct, totals),
        textprops=dict(color="w"),
        colors=['#89D2DC', 
                '#6564DB', 
                '#232ED1', 
                '#101D42', 
                '#0D1317', 
                '#6340B9', 
                '#3DE5E3', 
                '#071C5E', 
                '#6C7592', 
                '#5603CD', 
                '#DDC5FF', 
                '#1B0D2F', 
                '#3C5BE6', 
                '#7281C1', 
                '#064042', 
                '#931EBF', 
                '#F700E8'
                ]
        )
    ax.legend(values,loc="lower left")

    #putting the chart onto tkinter
    chart = FigureCanvasTkAgg(fig,frame)
    chart.get_tk_widget().pack(side='bottom',fill='both',expand=True)
    button = Button(frame, 
                    width = 25, 
                    command = lambda: remove_figures(canvas=chart,button=button), 
                    text = "Go Back!", pady=10)
    button.place(x=10,y=10)

# just prints it for now
def create_bar(frame,data,title):
    print(title)
    values, totals = np.unique(data, return_counts=True)
    print(values, totals)