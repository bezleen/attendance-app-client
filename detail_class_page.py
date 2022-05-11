import tkinter as tk
import execute_api.list_class as lc
import execute_api.list_attendance as la


class DetailClassPage(tk.Frame):

    def __init__(self, parent, controller, at=None, rt=None, datas=[]):
        tk.Frame.__init__(self, parent)
        self.container = parent
        self.controller = controller
        self.at = at
        self.rt = rt
        self.datas = datas
        self.class_id = datas[0]['class_id']
        try:
            print(datas[0]['class_id'])
        except:
            pass
        self.init_UI()
    def init_UI(self):
        self.label_date = tk.Label(self, text="Date")
        self.entry_date = tk.Entry(self, width=20, bg="light yellow")
        self.label_notice = tk.Label(self, text="", bg="orange")

        button_home = tk.Button(
            self, text="BACK", command=lambda: self.controller.show_frame(self.container, "ClassPage", self.at, self.rt))
        button_home.configure(width=10, bg="orange")

        button_all = tk.Button(
            self, text="ALL", command=self.list_attendance_all)
        button_all.configure(width=10, bg="lightblue")

        button_absent = tk.Button(
            self, text="ABSENT", command=self.list_attendance_absent)
        button_absent.configure(width=10, bg="lightblue")

        button_attendance = tk.Button(
            self, text="ATTENDANCE", command=self.list_attendance_attendance)
        button_attendance.configure(width=10, bg="lightblue")

        

        button_home.pack()
        button_all.pack()
        button_absent.pack()
        button_attendance.pack()
        self.label_date.pack()
        self.entry_date.pack()
        self.label_notice.pack()

    def list_attendance_all(self):
        # check date
        state="all"
        date = self.entry_date.get()
        if not date and state != "all":
            self.label_notice['text'] = "Please enter date"
            return
        date = date+"T00:00:00.00000"
        try:
            response = la.exec_list_attendance(
                self.at, self.class_id, state, date)
            if response['status'] == 200:
                # tao bang
                print(response['data'])
        except:
            pass
    def list_attendance_absent(self):
        # check date
        state="absent"
        date = self.entry_date.get()
        if not date :
            self.label_notice['text'] = "Please enter date"
            return
        date = date+"T00:00:00.00000"
        try:
            response = la.exec_list_attendance(
                self.at, self.class_id, state, date)
            if response['status'] == 200:
                # tao bang
                print(response['data'])
        except:
            pass
    def list_attendance_attendance(self):
        # check date
        state="attendance"
        date = self.entry_date.get()
        if not date:
            self.label_notice['text'] = "Please enter date"
            return
        date = date+"T00:00:00.00000"
        try:
            response = la.exec_list_attendance(
                self.at, self.class_id, state, date)
            if response['status'] == 200:
                # tao bang
                print(response['data'])
        except:
            pass