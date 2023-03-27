'''
Andre Arcaina  | Student ID: 501157540
Adam Begagic   | Student ID: 501155113
Joseph Leung   | Student ID: 501160939
Lauren Griffin | Student ID: 501098426
'''

from tkinter import *                          # library for GUI elements
from graph import (create_pie, create_bar)     # import functions from graph.py
from readcsv import *                          # use variables from read_csv file

'''
    main file with GUI elements
    creates a window with buttons to check graphs
'''

class Window:
    def __init__(self,root):
        # title, resolution, background colour
        self.root = root

        self.root.title("ChatGPT Survey GUI")
        self.root.geometry('1900x950')
        self.root.configure(background="#5A5A5A")
        self.root.resizable(True,True)

        l_title         = Label(self.root,
                                bg = "#5A5A5A",
                                fg = "white",
                                text= "Click a button to check a graph!", 
                                font = ("Georgia", 25))
    
        # button initializations
        # add action events for each button later    
        b_age           = Button(self.root, 
                                width = 25, 
                                command = lambda: create_pie(self.root,AGE[1:],AGE[0]), 
                                text = "What is your age?", pady=50, font=("Georgia", 10))

        b_department    = Button(self.root, 
                                width = 25, 
                                command = lambda: create_pie(self.root,DEPARTMENT[1:],DEPARTMENT[0]), 
                                text = "What Department?", pady=50, font=("Georgia", 10))

        b_heard         = Button(self.root, 
                                width = 25, 
                                command = lambda: create_pie(self.root,HEARD[1:],HEARD[0]), 
                                text = "Have you Heard of ChatGPT?", pady=50, font=("Georgia", 10))
        
        b_usage         = Button(self.root, 
                                width = 25, 
                                command = lambda: create_bar(self.root,USAGE[0],"USED"), 
                                text = "How have you Used ChatGPT?", pady=50, font=("Georgia", 10))
        
        b_improvement   = Button(self.root, 
                                width = 25, 
                                command = lambda: create_bar(self.root,None,"IMPROVEMENT"), 
                                text = "Any Improvement from ChatGPT?", pady=50, font=("Georgia", 10))
        
        b_reliability   = Button(self.root, 
                                width = 25, 
                                command = lambda: create_pie(self.root,RELIABILITY[1:],RELIABILITY[0]), 
                                text = "How Reliable is ChatGPT?", pady=50, font=("Georgia", 10))
        
        b_learning      = Button(self.root, 
                                width = 25, 
                                command = lambda: create_pie(self.root,LEARNING[1:],LEARNING[0]), 
                                text = "Learnt from ChatGPT?", pady=50, font=("Georgia", 10))
    
        b_dishonesty    = Button(self.root, 
                                width = 25, 
                                command = lambda: create_pie(self.root,DISHONESTY[1:],DISHONESTY[0]), 
                                text = "Academic Dishonesty?", pady=50, font=("Georgia", 10))
    

        b_assistance    = Button(self.root, 
                                width = 25, 
                                command = lambda: create_bar(self.root,ASSISTANCE[0],"ASSISTED"), 
                                text = "What kind of Assistance?", pady=50, font=("Georgia", 10))

        # place where they are on the GUI (x, y)
        l_title.place(x=710, y=0)
        b_age.place(x=510, y=50)
        b_department.place(x=730, y=50)
        b_heard.place(x=950, y=50)
        b_usage.place(x=1170, y=50)
        b_improvement.place(x=510, y=200)
        b_learning.place(x=730, y=200)
        b_reliability.place(x=950, y=200)
        b_dishonesty.place(x=1170, y=200)
        b_assistance.place(x=830, y=350)

if __name__ == '__main__':
    root = Tk()
    GUI = Window(root)
    GUI.root.mainloop()