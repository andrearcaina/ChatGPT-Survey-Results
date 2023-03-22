from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # for drawing graphs on tkinter
import matplotlib.pyplot as plt                                 # library for graphing data
import numpy as np                                              # library for entering data
from tkinter import Button                                      # import Button
from readcsv import remove_spaces                               # get specific function

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

    fig, ax = plt.subplots(figsize=(5,5)) #figsize is height and width of the figure

    fig.set_facecolor('#5A5A5A') #color of figure background
    ax.set_title(title, loc='center', wrap=True, color="w") #title of figure
    
    #setting up the pie
    ax.pie(
        totals, 
        radius=1,
        autopct= lambda pct: percentage(pct, totals),
        textprops=dict(color="w"),
        colors=['#89D2DC', 
                '#6564DB', 
                '#232ED1', 
                '#101D70', 
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
    
    #putting button on canvas and calling
    #the remove_figures function to remove both of them
    #to go back to the previous screen
    button = Button(frame, 
                    width = 25, 
                    command = lambda: remove_figures(canvas=chart,button=button), 
                    text = "Go Back!", pady=10)
    button.place(x=10,y=10)

# just prints it for now
def create_bar(frame,question):
    if question == "USED":
        majors = ['Architecture', 'Arts', 'Business', 'Community Service', 'Economics', 'Engineering', 'Human Geography', 'Math and Science', 'Mathematics', 'Science', 'Science and Business']
        y1_HaveNotUsed = [1, 5, 5, 2, 2, 6, 0, 2, 0, 21, 0]
        y2_No = [0, 3, 2, 3, 0, 1, 0, 0, 1, 5, 1]
        y3_Yes = [0, 2, 2, 0, 0, 4, 1, 0, 0, 17, 0]

        newBottom = [1,8,7,5,2,7,0,2,1,26,1]

        fig, ax = plt.subplots(figsize=(10,6)) #figsize is height and width of the figure

        # create a stacked bar graph
        plt.bar(majors, y1_HaveNotUsed, color = '#064042', label='I have not used ChatGPT for academia')
        plt.bar(majors, y2_No, bottom=y1_HaveNotUsed, color = '#7281C1', label='No')
        plt.bar(majors, y3_Yes, bottom=newBottom, color = '#931EBF', label='Yes')

        # add title and axis labels
        plt.title("Improvement in Grade vs. Student Majors")
        plt.xlabel('Majors')
        plt.ylabel('Number of Students')

        # add legend
        plt.legend()

        #putting the chart onto tkinter
        chart = FigureCanvasTkAgg(fig,frame)
        chart.get_tk_widget().pack(side='bottom',fill='both',expand=True)
        
        #putting button on canvas and calling
        #the remove_figures function to remove both of them
        #to go back to the previous screen
        button = Button(frame, 
                        width = 25, 
                        command = lambda: remove_figures(canvas=chart,button=button), 
                        text = "Go Back!", pady=10)
        button.place(x=10,y=10)


    if question == "ASSISTED":
        pass