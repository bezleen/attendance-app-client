import tkinter as tk
import execute_api.add_student_class as astc


class AddStudentClassPage(tk.Frame):

    def __init__(self, parent, controller, at=None, rt=None, datas=[]):
        tk.Frame.__init__(self, parent)
        self.container = parent
        self.controller = controller
        self.at = at
        self.rt = rt
        self.class_id = datas[0]['class_id']
        self.student_id = ""
        self.init_UI()

    def init_UI(self):
        label_title = tk.Label(self, text="REGISTER STUDENT")
        label_email = tk.Label(self, text="email")
        label_student_id = tk.Label(self, text="student_id")
        label_name = tk.Label(self, text="name")
        self.label_notice = tk.Label(self, text="", bg="orange")

        self.entry_email = tk.Entry(self, width=20, bg="light yellow")
        self.entry_student_id = tk.Entry(self, width=20, bg="light yellow")
        self.entry_name = tk.Entry(self, width=20, bg="light yellow")

        self.button_register = tk.Button(
            self, text="REGISTER", command=self.exe_register_student)
        self.button_register.configure(width=10, bg="orange")
        self.button_register_face = tk.Button(
            self, text="REGISTER FACE", command=self.exe_register_student_face)
        self.button_register_face.configure(width=10, bg="orange")
        self.button_done = tk.Button(self, text="DONE", command=self.done)
        self.button_done.configure(width=10, bg="orange")
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

        self.button_register.pack()
        # self.button_register_face.pack()
        self.button_back.pack()

    def exe_register_student(self):
        email = self.entry_email.get()
        name = self.entry_name.get()
        student_id = self.entry_student_id.get()
        if not name or not email or not student_id:
            self.label_notice['text'] = "Please fill the entry"
            return
        try:
            response = astc.add_student_class(
                self.at, email, student_id, name, self.class_id)
            print(response)
            if response['status'] == 200:
                self.student_id = response['data']['id']
                self.button_register.pack_forget()
                self.button_back.pack_forget()
                self.button_register_face.pack()
                self.label_notice['text'] = response['msg']
            else:
                self.label_notice['text'] = response['msg']
        except:
            self.label_notice['text'] = "SERVER ERROR"

    def exe_register_student_face(self):
        pass

    def done(self):
        pass
