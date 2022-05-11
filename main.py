import tkinter as tk
import execute_api.login as lg
import execute_api.signup as su

from start_page import StartPage
from register_page import RegisterPage
from home_page import HomePage
from class_page import ClassPage
from detail_class_page import DetailClassPage
from add_student_class import AddStudentClassPage
from take_attendance import TakeAttendancePage
from add_class import AddClassPage
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("BezleenApp")
        self.geometry("1600x900")
        self.resizable(width=False, height=False)

        container = tk.Frame()

        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        
        self.frames = {}
        for F in (StartPage,RegisterPage):
            page_name= F.__name__
            frame=F(parent=container,controller=self) 
            self.frames[page_name]=frame

            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(container,"StartPage")
        
    # def init_all_page(self,container,at,rt):
    #     for F in (HomePage,ClassPage):
    #         page_name= F.__name__
    #         frame=F(parent=container,controller=self, at=at,rt=rt) 
    #         self.frames[page_name]=frame

    #         frame.grid(row=0,column=0,sticky="nsew")

    def show_frame(self, container,page_name,at=None,rt=None,datas=[]):
        #del old frames
        try:
            del self.frames[page_name]
        except:
            pass
        #create new frame
        cls = globals()[page_name]
        frame=cls(parent=container,controller=self, at=at,rt=rt,datas=datas) 
        self.frames[page_name]=frame
        frame.grid(row=0,column=0,sticky="nsew")
        #show frame
        frame=self.frames[page_name]
        frame.tkraise()

    def close_app(self):
        self.destroy()


app = App()
app.mainloop()
