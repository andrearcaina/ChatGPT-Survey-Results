from tkinter import *   # library for GUI elements

class Window(Tk):
    def __init__(self):
        super().__init__()

        # UI elements
        self.title("ChatGPT Survey GUI")
        self.geometry('800x800')
        self.configure(background="light gray")

        self.l_title = Label(self, bg = "light gray", text="Click a button to check a graph!", font = ("Georgia", 25)).place(x=150, y=0)

        # button initializations
        # add action events for each button later
        b_age           = Button(self, width = 27, text = "How Old?", pady=10).place(x=0, y=50)

        b_department    = Button(self, width = 27, text = "What Department?", pady=10).place(x=200, y=50)

        b_heard         = Button(self, width = 27, text = "Have you Heard of ChatGPT?", pady=10).place(x=400, y=50)
        
        b_usage         = Button(self, width = 27, text = "How have you Used ChatGPT?", pady=10).place(x=600, y=50)
        
        b_improvement   = Button(self, width = 27, text = "Any Improvement from ChatGPT?", pady=10).place(x=0, y=100)
        
        b_reliability   = Button(self, width = 27, text = "How Reliable is ChatGPT?", pady=10).place(x=200, y=100)
        
        b_learning      = Button(self, width = 27, text = "Learnt from ChatGPT?", pady=10).place(x=400, y=100)
        
        b_dishonesty    = Button(self, width = 27, text = "Academic Dishonesty?", pady=10).place(x=600, y=100)
        
        b_assistance    = Button(self, width = 27, text = "What kind of Assistance?", pady=10).place(x=300, y=150)

        # button functionality
        # will display graph
        def display(self,data,title):
            pass

if __name__ == '__main__':
    GUI = Window()
    GUI.mainloop()