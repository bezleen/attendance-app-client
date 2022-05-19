import tkinter as tk
import execute_api.take_attendance as ta
import execute_api.add_student_into_class as atic
import execute_api.refresh as rf
class TakeAttendancePage(tk.Frame):

    def __init__(self, parent, controller, at=None, rt=None, datas=[]):
        tk.Frame.__init__(self, parent)
        self.container = parent
        self.controller = controller
        self.at = at
        self.rt = rt

        self.class_id = datas[0]['class_id']
        self.student_oid=datas[0]['student_oid']
        self.name=datas[0]['name']
        self.email=datas[0]['email']
        self.student_id=datas[0]['student_id']

        self.init_UI()

    def init_UI(self):
        label_title = tk.Label(self, text="CONFIRM STUDENT")
        label_email = tk.Label(self, text="email")
        label_student_id = tk.Label(self, text="student_id")
        label_name = tk.Label(self, text="name")
        self.label_notice = tk.Label(self, text="", bg="orange")

        self.entry_email = tk.Entry(self,width=20, bg="light yellow")
        self.entry_email.insert(tk.END, self.email)
        self.entry_student_id = tk.Entry(self, width=20, bg="light yellow")
        self.entry_student_id.insert(tk.END, self.student_id)
        self.entry_name = tk.Entry(self, width=20, bg="light yellow")
        self.entry_name.insert(tk.END, self.name)

        self.button_confirm = tk.Button(
            self, text="CONFIRM", command=self.take_attendance)
        self.button_confirm.configure(width=10, bg="orange")
        

        self.button_join = tk.Button(
            self, text="JOIN", command=self.join_class)
        self.button_join.configure(width=10, bg="orange")


        self.button_back = tk.Button(self, text="BACK", command=lambda: self.controller.show_frame(
            self.container,
            "DetailClassPage",
            self.at,
            self.rt,
            [{"class_id": self.class_id}]
        ))
        self.button_back.configure(width=10, bg="orange")

        label_title.pack()

        label_email.pack()
        self.entry_email.pack()

        label_student_id.pack()
        self.entry_student_id.pack()

        label_name.pack()
        self.entry_name.pack()

        self.label_notice.pack()

        self.button_confirm.pack()
        self.button_back.pack()

    
    def take_attendance(self):
        self.check_current_token()

        #check student inclass
        try:
            response=ta.add_sheet(self.at,self.student_oid,self.class_id)
            if response['status'] == 200:
                self.label_notice['text'] = response['msg']
            elif response['status'] == 400 and response['msg'] == "Student not in class": 
                self.label_notice['text'] = "You're not in this class, do you want to join?"
                #hien nut join
                self.button_join.pack()
                #an nut confirm
                self.button_confirm.pack_forget()
        except:
            self.label_notice['text'] = "Server error"
    def join_class(self):
        self.check_current_token()
        #add vao lop
        try:
            response=atic.add_student_into_class(self.at,self.student_oid,self.class_id)
            if response['status'] == 200:
                self.label_notice['text'] = response['msg']
                #an nut join
                self.button_join.pack_forget()
                #hien nut confirm
                self.button_confirm.pack()
            else:
                self.label_notice['text'] = response['msg']
        except:
            self.label_notice['text'] = "Server error"



    def check_current_token(self):
        new_at,new_rt,status= rf.check_token(self.at,self.rt)
        if not new_at and not new_rt and not status:
            pass
        elif new_at and new_rt and not status:
            self.at = new_at
            self.rt = new_rt
        elif not new_at and not new_rt and status=='restart':
            self.controller.show_frame(self.container,"StartPage",self.at,self.rt)

