import tkinter as tk
# import execute_api.login as lg
import execute_api.signup as su

class RegisterPage(tk.Frame):

    def __init__(self, parent,controller,at=None,rt=None,datas=[]):
        tk.Frame.__init__(self, parent)
        self.container=parent
        self.controller = controller
        self.at = at
        self.rt = rt
        self.init_UI()
    def init_UI(self):
        label_title = tk.Label(self, text="SIGN IN")
        label_email = tk.Label(self, text="email")
        label_phone = tk.Label(self, text="phone")
        label_username = tk.Label(self, text="username")
        label_pw = tk.Label(self, text="password")
        label_cfpw = tk.Label(self, text="confirm password")

        self.label_notice = tk.Label(self, text="", bg="orange")
        self.entry_email = tk.Entry(self, width=20, bg="light yellow")
        self.entry_phone = tk.Entry(self, width=20, bg="light yellow")
        self.entry_username = tk.Entry(self, width=20, bg="light yellow")
        self.entry_pw = tk.Entry(self, width=20, bg="light yellow")
        self.entry_cfpw = tk.Entry(self, width=20, bg="light yellow")

        button_log = tk.Button(self, text="SIGN IN", command=self.exe_signup)
        button_log.configure(width=10, bg="orange")
        button_back = tk.Button(self, text="BACK", command=lambda: self.controller.show_frame(self.container,"StartPage",self.at,self.rt))
        button_back.configure(width=10, bg="orange")

        label_title.pack()

        label_email.pack()
        self.entry_email.pack()

        label_phone.pack()
        self.entry_phone.pack()

        label_username.pack()
        self.entry_username.pack()

        label_pw.pack()
        self.entry_pw.pack()

        label_cfpw.pack()
        self.entry_cfpw.pack()

        self.label_notice.pack()

        button_log.pack()
        button_back.pack()

    def exe_signup(self):
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        name = self.entry_username.get()
        password = self.entry_pw.get()
        cf_password = self.entry_cfpw.get()
        if password == cf_password:
            try:
                response = su.exec_signup(email, password,name,phone)
                if response['status'] == 200:
                    self.label_notice['text'] = response['msg']
                    #chuyen sang trang dang nhap
                    self.controller.show_frame(self.container,"StartPage",self.at,self.rt)
                else:
                    self.label_notice['text'] = response['msg']
            except:
                self.label_notice['text'] = "Register failed"
        else:
            self.label_notice['text'] = "Wrong confirm password."
