import tkinter as tk
import execute_api.login as lg
import execute_api.refresh as rf

class StartPage(tk.Frame):

    def __init__(self, parent,controller,at=None,rt=None,datas=[]):
        tk.Frame.__init__(self, parent)
        self.container=parent
        self.controller = controller
        self.at = at
        self.rt = rt
        self.init_UI()
    def init_UI(self):
        #label
        label_title = tk.Label(self, text="LOG IN")
        label_user = tk.Label(self, text="username")
        label_pw = tk.Label(self, text="password")
        #entry
        self.label_notice = tk.Label(self, text="", bg="orange")
        self.entry_user = tk.Entry(self, width=20, bg="light yellow")
        self.entry_pw = tk.Entry(self,show='*', width=20, bg="light yellow")
        #button
        button_log = tk.Button(self, text="LOG IN", command=self.exe_login)
        button_log.configure(width=10, bg="orange")
        button_sig = tk.Button(self, text="SIGN UP", command= lambda: self.controller.show_frame(self.container,"RegisterPage",self.at,self.rt))
        button_sig.configure(width=10, bg="orange")
        button_fpwd = tk.Button(self, text="FORGOT PWD", command= lambda: self.controller.show_frame(self.container,"ResetPasswordPage",self.at,self.rt))
        button_fpwd.configure(width=10, bg="orange")
        #show
        label_title.pack()
        label_user.pack()
        self.entry_user.pack()
        label_pw.pack()
        self.entry_pw.pack()
        self.label_notice.pack()

        button_log.pack()
        button_sig.pack()
        button_fpwd.pack()

    def exe_login(self):
        email = self.entry_user.get()
        password = self.entry_pw.get()
        # email="hiendang@heallios.com"
        # password = "456789"
        try:
            response = lg.exec_login(email, password)
            if response['status'] == 200:
                self.at = response['data']['access_token']
                self.rt = response['data']['refresh_token']
                rf.write_token(self.at, self.rt)
                #chuyen vao home page
                # self.controller.init_all_page(self.container,self.at, self.rt)
                self.controller.show_frame(self.container,"HomePage",self.at, self.rt)
            else:
                self.label_notice['text'] = response['msg']
        except:
            self.label_notice['text'] = "Not a valid email address."

