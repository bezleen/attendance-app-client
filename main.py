import tkinter as tk
import execute_api.login as lg
import execute_api.signup as su


class StartPage(tk.Frame):

    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        at = ''
        rt = ''
        #label
        label_title = tk.Label(self, text="LOG IN")
        label_user = tk.Label(self, text="username")
        label_pw = tk.Label(self, text="password")
        #entry
        self.label_notice = tk.Label(self, text="", bg="orange")
        self.entry_user = tk.Entry(self, width=20, bg="light yellow")
        self.entry_pw = tk.Entry(self, width=20, bg="light yellow")
        #button
        button_log = tk.Button(self, text="LOG IN", command=self.exe_login)
        button_log.configure(width=10, bg="orange")
        button_sig = tk.Button(self, text="SIGN UP", command= lambda: controller.show_frame("RegisterPage"))
        button_sig.configure(width=10, bg="orange")
        #show
        label_title.pack()
        label_user.pack()
        self.entry_user.pack()
        label_pw.pack()
        self.entry_pw.pack()
        self.label_notice.pack()

        button_log.pack()
        button_sig.pack()

    def exe_login(self):
        email = self.entry_user.get()
        password = self.entry_pw.get()

        try:
            response = lg.exec_login(email, password)
            if response['status'] == 200:
                self.at = response['data']['access_token']
                self.rt = response['data']['refresh_token']
                #chuyen vao home page
            else:
                self.label_notice['text'] = response['msg']
        except:
            self.label_notice['text'] = "Not a valid email address."


class RegisterPage(tk.Frame):

    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        at = ''
        rt = ''

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
                    self.controller.show_frame("StartPage")
                else:
                    self.label_notice['text'] = response['msg']
            except:
                self.label_notice['text'] = "Register failed"
        else:
            self.label_notice['text'] = "Wrong confirm password."

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

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame=self.frames[page_name]
        frame.tkraise()

    def close_app(self):
        self.destroy()


app = App()
app.mainloop()
