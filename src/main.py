from tkinter import * # library for GUI elements

class Window:
    def __init__(self,root):
        self.root = root

        # UI elements
        self.root.title("ChatGPT Survey Data")
        self.root.geometry('800x600')

        # button initializations
        # add action events for each button later
        b_Age           = Button(self.root, width = 27, text = "How Old?", pady=10).grid(row=0, column=0)

        b_department    = Button(self.root, width = 27, text = "What Department?", pady=10).grid(row=1, column=0)

        b_heard         = Button(self.root, width = 27, text = "Have you Heard of ChatGPT?", pady=10).grid(row=2, column=0)
        
        b_usage         = Button(self.root, width = 27, text = "How have you Used ChatGPT?", pady=10).grid(row=3, column=0)
        
        b_improvement   = Button(self.root, width = 27, text = "Any Improvement from ChatGPT?", pady=10).grid(row=4, column=0)
        
        b_reliability   = Button(self.root, width = 27, text = "How Reliable is ChatGPT?", pady=10).grid(row=5, column=0)
        
        b_learning      = Button(self.root, width = 27, text = "Learnt from ChatGPT?", pady=10).grid(row=6, column=0)
        
        b_dishonesty    = Button(self.root, width = 27, text = "Academic Dishonesty?", pady=10).grid(row=7, column=0)
        
        b_assistance    = Button(self.root, width = 27, text = "What kind of Assistance?", pady=10).grid(row=8, column=0)

        # button functionality
        # will display graph
        def plot_values(self,data,title):
            pass

if __name__ == '__main__':
    root = Tk()
    GUI = Window(root)
    GUI.root.mainloop()