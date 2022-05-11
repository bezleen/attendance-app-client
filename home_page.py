import tkinter as tk


class HomePage(tk.Frame):

    def __init__(self, parent,controller,at=None,rt=None,datas=[]):
        tk.Frame.__init__(self, parent)
        self.container=parent
        self.controller = controller
        self.at = at
        self.rt = rt
        self.init_UI()
    def init_UI(self):
        
        button_class = tk.Button(self, text="CLASS",command=lambda: self.controller.show_frame(self.container,"ClassPage",self.at,self.rt))
        button_class.configure(width=10, bg="orange")

        button_class.pack()


    