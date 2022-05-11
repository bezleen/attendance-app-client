import tkinter as tk
import execute_api.list_class as lc


class DetailClassPage(tk.Frame):

    def __init__(self, parent, controller, at=None, rt=None,datas=[]):
        tk.Frame.__init__(self, parent)
        self.container = parent
        self.controller = controller
        self.at = at
        self.rt = rt
        self.init_UI()
        self.datas= datas
        try:
            print(datas[0]['class_id'])
        except:
            pass
    def init_UI(self):

        button_home = tk.Button(
            self, text="BACK", command=lambda: self.controller.show_frame(self.container,"ClassPage",self.at,self.rt))
        button_home.configure(width=10, bg="orange")

        button_home.pack()


