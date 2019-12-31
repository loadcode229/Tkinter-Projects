from tkinter import Tk, Label, Button, W #LEFT, RIGHT

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.grid(columnspan=2, sticky=W)
        #self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.grid(row=1)
        #self.greet_button.pack(side=LEFT)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=1, column=1)
        #self.close_button.pack(side=RIGHT)

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
