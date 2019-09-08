from Tkinter import *

class display:
    def __init__(self, master):
        self.var = IntVar()
        frame = Frame(master)
        frame.grid()
        f2 = Frame(master,width=200,height=100)
        f2.grid(row=0,column=1)
        button = Checkbutton(frame,text='show',variable=self.var,command=self.fx)
        button.grid(row=0,column=0)
        msg2="""I feel bound to give them full satisfaction on this point"""
        self.v= Message(f2,text=msg2)
    def fx(self):
        if self.var.get():
            self.v.grid(column=1,row=0,sticky=N)
        else:
            self.v.grid_remove()

top = Tk()
app = display(top)            
top.mainloop()

'''
import Tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there['text'] = "Hello World\n(click me)"
        self.hi_there['command'] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text='QUIT', fg='red',
                              command=self.master.destroy)
        self.quit.pack(side='bottom')

    def say_hi(self):
        print('hi there, everyone!')

root = tk.Tk()
app = Application(master=root)
app.mainloop()

'''