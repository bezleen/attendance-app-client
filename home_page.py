import tkinter as tk
import execute_api.refresh as rf

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
        # button_logout = tk.Button(self, text="LOGOUT",command=lambda: self.controller.show_frame(self.container,"StartPage",self.at,self.rt))
        button_logout = tk.Button(self, text="LOGOUT",command=self.logout)
        button_logout.configure(width=10, bg="orange")
        button_profile = tk.Button(self, text="PROFILE")
        button_profile.configure(width=10, bg="orange")

        button_class.pack()
        button_profile.pack()
        button_logout.pack()


    def logout(self):
        rf.write_token('','')
        self.controller.show_frame(self.container,"StartPage",self.at,self.rt)