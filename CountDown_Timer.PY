# Mr. suman kalyan pradhan
# Minor Project
'''
Minor Project Statement : Create A Countdown Timer Using Python
Features Included : Reset / Stop & Pause / Resume
'''

import tkinter as tk
from tkinter import *
from tkinter import messagebox


class Application: 
    def __init__(self, root, *args, **kwargs):
        self.root = root
        self.running = False
        self.time = 0
        self.hours = 0
        self.mins = 0
        self.secs = 0
        self.build_interface()

    def build_interface(self):
        title = Label(self.root,
                      text=" COUNTDOWN TIMER " ,
                      font= '"arial" 20 bold italic' ,
                      bg="#99d3ff" ,
                      fg= "black" ,
                      bd= 5 ,
                      relief=RAISED)
        title.place(relwidth= 1 , y = 2 )
        
        # ENTRY
        self.time_entry = Entry(self.root)
        self.time_entry.place(x = 300 , y = 60)


        # LABELS
        self.clock = Label(self.root,
                           text="00:00:00",
                           font=('Courier', 30) ,
                           bg = 'pink' ,
                           width=20)
        self.clock.place(x = 120 , y = 90)

        self.time_label = Label(self.root,
                                text="hour   min   sec",
                                font=("Courier", 10),
                                width=40 ,
                                fg='#FFFF8A' ,
                                bg = 'black')
        self.time_label.place(x = 195 , y = 150)


        # BUTTONS
        self.start_button = Button(self.root, text=" START " ,
                                   relief= RAISED ,
                                   cursor= "hand2" ,
                                   width= 7,
                                   font='"times new roman" 15' ,
                                   bg = "#ff1a40" ,
                                   fg= 'black',
                                   command=lambda: self.start())
        self.start_button.place(x = 60 , y = 250)

        self.reset_button = Button(self.root, text=" RESET " ,
                                   relief= RAISED ,
                                   cursor= "hand2" ,
                                   width= 7, font='"times new roman\" 15' ,
                                   bg = "#ff1a40" ,
                                   fg= 'black' ,
                                   command=lambda: self.reset())
        self.reset_button.place(x = 230 , y = 250)
        
        self.pause_button = Button(self.root, text=" PAUSE " ,
                                   relief= RAISED ,
                                   cursor= "hand2" ,
                                   width= 7,
                                   font='"times new roman\" 15' ,
                                   bg = "#ff1a40" ,
                                   fg= 'black',
                                   command=lambda: self.pause())
        self.pause_button.place(x = 390 , y = 250)

        self.quit_button = Button(self.root, text=" QUIT " ,
                                  relief= RAISED ,
                                  cursor= "hand2" ,
                                  width= 7,
                                  font='"times new roman\" 15' ,
                                  bg = "#ff1a40" ,
                                  fg= 'black',
                                  command=lambda: self.quit())
        self.quit_button.place(x = 560 , y = 250)


        self.root.bind("<Return>", lambda x: self.start())
        self.time_entry.bind("<Key>", lambda v: self.update())

    def calculate(self):
        self.hours = self.time // 3600
        self.mins = (self.time // 60) % 60
        self.secs = self.time % 60
        return "{:02d}:{:02d}:{:02d}".format(self.hours, self.mins, self.secs)





    def update(self):
        self.time = self.time_entry.get()
        try:
            self.clock.configure(text=self.calculate())
        except:
            self.clock.configure(text="00:00:00")

    def timer(self):
        if self.running:
            if self.time <= 0:
                self.clock.configure(text="Time's up!")
            else:
                self.clock.configure(text=self.calculate())
                self.time -= 1
                self.root.after(1000, self.timer)


# START TIMER
    def start(self):
        try:
            self.time = int(self.time_entry.get())
            self.time_entry.delete(0, 'end')
        except:
            self.time = self.time
        self.start_button.configure(relief= RIDGE , bg = "#1affdb")
        self.pause_button.configure(relief= RAISED, bg = "#ff1a40",
                                    command=lambda: self.pause())
        self.reset_button.configure(relief= RAISED,bg = "#ff1a40" )
        self.quit_button.configure(relief= RAISED, bg = "#ff1a40")
        self.root.bind("<Return>", lambda x: self.pause())
        self.running = True
        self.timer()


# RESET TIMER
    def reset(self):
        if self.running:
            self.start_button.configure(text='START',
                                        width = 7,
                                        relief= RAISED,
                                        bg = "#ff1a40",
                                        command=lambda: self.start())
            self.pause_button.configure(relief= RAISED, bg = "#ff1a40")
            self.reset_button.configure(relief= RIDGE , bg = "#1affdb")
            self.quit_button.configure(relief= RAISED, bg = "#ff1a40")
            self.start_button.configure(text=" START ",
                                        command=lambda: self.start())
            self.root.bind("<Return>", lambda x: self.start())
            self.running = False
        self.running = False
        self.time = 0
        self.clock["text"] = "00:00:00"

        
        self.start_button.configure(text='START',
                                    width = 7,
                                    relief= RAISED,
                                    bg = "#ff1a40")
        self.pause_button.configure(relief= RAISED, bg = "#ff1a40")
        self.reset_button.configure(relief= RAISED, bg = "#ff1a40")


# PAUSE TIMER
    def pause(self):
        self.root.bind("<Return>", lambda x: self.start())
        if self.running == True:
            self.start_button.configure(text='RESUME' , width = 8,
                                        relief= RAISED,
                                        bg = "#ff1a40",
                                        command=lambda: self.start())
            self.pause_button.configure(relief= RIDGE, bg = "#1affdb")
            self.reset_button.configure(relief= RAISED, bg = "#ff1a40")
            self.quit_button.configure(relief= RAISED, bg = "#ff1a40")
            self.running = False
        self.timer()
      
      
# RESUME TIMER
    def resume(self):
        """Resume timer"""
        self.pause_button.configure(text="PAUSE",
                                    command=lambda: self.start())
        self.root.bind("<Return>", lambda x: self.start())
        if self.running == False:
            self.running = True
        self.timer()
        
        
# QUIT TIMER
    def quit(self):
        """quit the window"""
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()


if __name__ == "__main__":
    """Main loop of timer"""
    root = tk.Tk()
    root.title("TIMER")
    root.geometry('700x300+450+200') 
    root.config(bg = '#FFFF8A')
    root.resizable(0 , 0)
    obj = Application(root)
    root.mainloop()
