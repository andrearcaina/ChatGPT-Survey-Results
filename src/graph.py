'''
Andre Arcaina  | Student ID: 501157540
Adam Begagic   | Student ID: 501155113
Joseph Leung   | Student ID: 501160939
Lauren Griffin | Student ID: 501098426
'''

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # for drawing graphs on tkinter
import matplotlib.pyplot as plt                                 # library for graphing data
import numpy as np                                              # library for entering data
from tkinter import Button                                      # import Button

'''
    this file contains all the functions 
    each function assists/displays the graphs onto the screen
'''

# colorway for the graphs
colors = [
        '#89D2DC', '#6564DB', '#232ED1', 
        '#101D70', '#0D1317', '#6340B9', 
        '#3DE5E3', '#071C5E', '#6C7592', 
        '#5603CD', '#DDC5FF', '#1B0D2F', 
        '#3C5BE6', '#7281C1', '#064042', 
        '#931EBF', '#F700E8'
        ]

# function that displays the graph and button onto the screen
def display(fig,frame):
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

# removes the graph and button from the screen when button clicked
def remove_figures(canvas,button):
    canvas.get_tk_widget().destroy()
    button.destroy()

# displays percentage based on parameters
def percentage(pct, allvals):
    absolute = int(np.round(pct / 100. * np.sum(allvals)))
    return "{:.1f}%".format(pct, absolute)

# creates a pie graph with the given parameters
def create_pie(frame,data,title):
    # gets the values from the data and the total of each value from the data
    values, totals = np.unique(data, return_counts=True)

    fig, ax = plt.subplots(figsize=(5,5)) #figsize is height and width of the figure

    fig.set_facecolor('#5A5A5A') #color of figure background
    ax.set_title(title, loc='center', wrap=True, color="w") #title of figure
    
    #setting up the pie
    ax.pie(
        totals, 
        radius=1,
        autopct= lambda pct: percentage(pct, totals),
        textprops=dict(color="w"),
        colors=colors,
        )
    ax.legend(values,loc="lower left")

    #calling display function to display graph and button
    display(fig,frame)

def create_bar(frame,title,question):
    if question == "IMPROVEMENT": #if the question is improvement
        majors = ['Architecture', 'Arts', 'Business', 'Community Service', 'Economics', 
                'Engineering', 'Human Geography', 'Math and Science', 'Mathematics', 
                'Science', 'Science and Business'
                ]
        option_NotUsed = [1, 5, 5, 2, 2, 6, 0, 2, 0, 21, 0]
        option_No = [0, 3, 2, 3, 0, 1, 0, 0, 1, 5, 1]
        option_Yes = [0, 2, 2, 0, 0, 4, 1, 0, 0, 17, 0]

        bottom = [1,8,7,5,2,7,0,2,1,26,1]

        fig, ax = plt.subplots(figsize=(20,6)) #figsize is height and width of the figure

        # create a stacked bar graph
        plt.bar(majors, option_NotUsed, color = colors[14], label='I have not used ChatGPT for academia')
        plt.bar(majors, option_No, bottom=option_NotUsed, color = colors[13], label='No')
        plt.bar(majors, option_Yes, bottom=bottom, color = colors[15], label='Yes')

        # add title and axis labels
        plt.title("Improvement in Grade vs. Student Majors")
        plt.xlabel('Majors')
        plt.ylabel('Number of Students')

        # add legend
        plt.legend()
        
        #calling display function to display graph and button
        display(fig,frame)


    if question == "ASSISTED" or question == "USED": #if question is assisted or used
        #options is for assisted
        options = ['Essay writing or inspiration','Mathematics assistance','proofreading assignments',
                'Summing up a topic','Research ideas','Grammar (vocab, syntax)','None',
                'Secondary Google','Programming']
        totals = [39,39,54,52,56,54,7,1,1]
        if question == "USED": #but if the question is used
            #option is now for used
            options = ['Academia','Entertainment', 'Personal', 'I have not Used ChatGPT']
            totals = [40,27,29,30] 

        fig, ax = plt.subplots(figsize=(20,6)) #figsize is height and width of the figure

        # create a horizontal bar graph
        plt.style.use('ggplot')
        plt.barh(options, totals, color = colors)
        plt.title(title)
        plt.ylabel('Options')
        plt.xlabel('Total People Inputted')
    
        # include the percentage and text for each bar
        for index, value in enumerate(totals):
            percentage = "{:.1f}%".format(value / 86 * 100)
            plt.text(value, index, f"{value} ({percentage})")

        # call display function and pass in fig and frame
        display(fig,frame)
