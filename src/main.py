from tkinter import *                          # library for GUI elements
from graph import (create_pie, create_bar)     # import functions from graph.py
from readcsv import *                          # use variables from read_csv file

class Window(Tk):
    def __init__(self):
        super().__init__()

        # title, resolution, background colour
        self.title("ChatGPT Survey GUI")
        self.geometry('800x800')
        self.configure(background="light gray")
        self.resizable(False,False)

        l_title         = Label(self, 
                                 bg = "light gray", 
                                 text= "Click a button to check a graph!", 
                                 font = ("Georgia", 25))
        
        # button initializations
        # add action events for each button later
        b_age           = Button(self, 
                                 width = 27, 
                                 command = lambda: create_pie(AGE[1:],AGE[0]), 
                                 text = "How Old?", pady=10)

        b_department    = Button(self, 
                                 width = 27, 
                                 command = lambda: create_pie(DEPARTMENT[1:],DEPARTMENT[0]), 
                                 text = "What Department?", pady=10)

        b_heard         = Button(self, 
                                 width = 27, 
                                 command = lambda: create_pie(HEARD[1:],HEARD[0]), 
                                 text = "Have you Heard of ChatGPT?", pady=10)
        
        b_usage         = Button(self, 
                                 width = 27, 
                                 command = lambda: create_bar(USAGE[1:],USAGE[0]), 
                                 text = "How have you Used ChatGPT?", pady=10)
        
        b_improvement   = Button(self, 
                                 width = 27, 
                                 command = lambda: create_pie(IMPROVEMENT[1:],IMPROVEMENT[0]), 
                                 text = "Any Improvement from ChatGPT?", pady=10)
        
        b_reliability   = Button(self, 
                                 width = 27, 
                                 command = lambda: create_pie(RELIABILITY[1:],RELIABILITY[0]), 
                                 text = "How Reliable is ChatGPT?", pady=10)
        
        b_learning      = Button(self, 
                                 width = 27, 
                                 command = lambda: create_pie(LEARNING[1:],LEARNING[0]), 
                                 text = "Learnt from ChatGPT?", pady=10)
       
        b_dishonesty    = Button(self, 
                                 width = 27, 
                                 command = lambda: create_pie(DISHONESTY[1:],DISHONESTY[0]), 
                                 text = "Academic Dishonesty?", pady=10)
       

        b_assistance    = Button(self, 
                                 width = 27, 
                                 command = lambda: create_bar(ASSISTANCE[1:],ASSISTANCE[0]), 
                                 text = "What kind of Assistance?", pady=10)

        # place where they are on the GUI (x, y)
        l_title.place(x=160, y=0)
        b_age.place(x=0, y=50)
        b_department.place(x=200, y=50)
        b_heard.place(x=400, y=50)
        b_usage.place(x=600, y=50)
        b_improvement.place(x=0, y=100)
        b_learning.place(x=400, y=100)
        b_reliability.place(x=200, y=100)
        b_dishonesty.place(x=600, y=100)
        b_assistance.place(x=300, y=150)

if __name__ == '__main__':
    GUI = Window()
    GUI.mainloop()