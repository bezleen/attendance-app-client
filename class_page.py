import tkinter as tk
from unicodedata import name
import execute_api.list_class as lc
import execute_api.refresh as rf

class ClassPage(tk.Frame):

    def __init__(self, parent, controller, at=None, rt=None, datas=[]):
        tk.Frame.__init__(self, parent)
        self.container = parent
        self.controller = controller
        self.at = at
        self.rt = rt
        self.init_UI()
        self.display_data()

    def init_UI(self):

        button_home = tk.Button(
            self, text="HOME", command=lambda: self.controller.show_frame(self.container, "HomePage", self.at, self.rt))
        button_home.configure(width=10, bg="orange")
        button_add = tk.Button(
            self, text="ADD ClASS",command=lambda: self.controller.show_frame(self.container, "AddClassPage", self.at, self.rt))
        button_add.configure(width=10, bg="orange")

        button_home.pack()
        button_add.pack()

    def display_data(self):
        self.check_current_token()

        # get data
        try:
            response = lc.exec_list_class(self.at)
            if response['status'] == 200:
                # display
                for i in response['data']:
                    button_class = tk.Button(
                        self, text=i['name'],
                        command=lambda name=i['id']: self.controller.show_frame(
                            self.container,
                            "DetailClassPage",
                            self.at,
                            self.rt,
                            [{"class_id": name}]
                        )
                    )
                    button_class.configure(width=50, bg="lightblue")
                    button_class.pack()
        except:
            pass
    
    def check_current_token(self):
        new_at,new_rt,status= rf.check_token(self.at,self.rt)
        if not new_at and not new_rt and not status:
            pass
        elif new_at and new_rt and not status:
            self.at = new_at
            self.rt = new_rt
        elif not new_at and not new_rt and status=='restart':
            self.controller.show_frame(self.container,"StartPage",self.at,self.rt)
