import tkinter as tk


import execute_api.send_otp as so
import execute_api.check_otp as co
import execute_api.reset_pass as rp
class ResetPasswordPage(tk.Frame):

    def __init__(self, parent,controller,at=None,rt=None,datas=[]):
        tk.Frame.__init__(self, parent)
        self.container=parent
        self.controller = controller
        self.at = at
        self.rt = rt
        self.init_UI()
        self.email=''
        self.otp=''
    def init_UI(self):
        self.label_title = tk.Label(self, text="FORGOT PASSWORD")
        self.label_email = tk.Label(self, text="email")
        self.label_otp = tk.Label(self, text="otp")
        self.label_pw = tk.Label(self, text="new password")
        self.label_cfpw = tk.Label(self, text="confirm password")

        self.label_notice = tk.Label(self, text="", bg="orange")

        self.entry_email = tk.Entry(self, width=20, bg="light yellow")
        self.entry_otp = tk.Entry(self, width=20, bg="light yellow")
        self.entry_pw = tk.Entry(self,show='*', width=20, bg="light yellow")
        self.entry_cfpw = tk.Entry(self,show='*', width=20, bg="light yellow")

        self.button_next1 = tk.Button(self, text="NEXT", command=self.exe_send_otp)
        self.button_next1.configure(width=10, bg="orange")

        self.button_next2 = tk.Button(self, text="NEXT", command=self.exe_check_otp)
        self.button_next2.configure(width=10, bg="orange")
        self.button_resend = tk.Button(self, text="RESEND", command=self.exe_resend_otp)
        self.button_resend.configure(width=10, bg="orange")

        self.button_next3 = tk.Button(self, text="NEXT", command=self.exe_reset_password)
        self.button_next3.configure(width=10, bg="orange")

        self.button_back = tk.Button(self, text="BACK", command=lambda: self.controller.show_frame(self.container,"StartPage",self.at,self.rt))
        self.button_back.configure(width=10, bg="orange")

        self.label_title.pack()
        self.label_notice.pack()
        #1
        self.label_email.pack()
        self.entry_email.pack()
        self.button_next1.pack()
        # #2
        # self.label_otp.pack()
        # self.entry_otp.pack()
        # self.button_next2.pack()
        # #3
        # self.label_pw.pack()
        # self.entry_pw.pack()
        # self.label_cfpw.pack()
        # self.entry_cfpw.pack()
        # self.button_next3.pack()
        

        self.button_back.pack()

    def exe_send_otp(self):
        email = self.entry_email.get()
        self.email=email
        if email:
            try:
                response=so.exec_send_otp(self.email)
                if response['status'] == 200:
                    self.label_email.pack_forget()
                    self.entry_email.pack_forget()
                    self.button_next1.pack_forget()
                    self.label_notice['text'] = "Check your email to get OTP"
                    self.label_otp.pack()
                    self.entry_otp.pack()
                    self.button_next2.pack()
                    self.button_resend.pack()
                else:
                    self.label_notice['text'] = response['msg']
            except:
                self.label_notice['text'] = "ERROR"
        else:
            self.label_notice['text'] = "Please entry email"
    def exe_resend_otp(self):
        if self.email:
            try:
                response=so.exec_send_otp(self.email)
                if response['status'] == 200:
                    self.label_email.pack_forget()
                    self.entry_email.pack_forget()
                    self.button_next1.pack_forget()
                    self.label_notice['text'] = "Check your email to get OTP"
                    self.label_otp.pack()
                    self.entry_otp.pack()
                    self.button_next2.pack()
                    self.button_resend.pack()
                else:
                    self.label_notice['text'] = response['msg']
            except:
                self.label_notice['text'] = "ERROR"
        else:
            self.label_notice['text'] = "Please entry email"
    def exe_check_otp(self):
        otp = self.entry_otp.get()
        self.otp=otp
        if otp:
            try:
                response=co.exec_check_otp(self.email,self.otp)
                if response['status'] == 200 and response['data']['correct']==True:
                    self.label_otp.pack_forget()
                    self.entry_otp.pack_forget()
                    self.button_next2.pack_forget()
                    self.button_resend.pack_forget()
                    self.label_notice['text'] = "You have 2 minute to change your password"
                    self.label_pw.pack()
                    self.entry_pw.pack()
                    self.label_cfpw.pack()
                    self.entry_cfpw.pack()
                    self.button_next3.pack()
                elif response['status'] == 200 and response['data']['correct']==False:
                    self.label_notice['text'] = "Wrong OTP"
                else:
                    self.label_notice['text'] = response['msg']
            except:
                self.label_notice['text'] = "ERROR"
        else:
            self.label_notice['text'] = "Please entry OTP"
    def exe_reset_password(self):
        password = self.entry_pw.get()
        cf_password = self.entry_cfpw.get()
        if password and cf_password:
            try:
                if password != cf_password:
                    self.label_notice['text'] = "Wrong confirm password."
                    return
                response=rp.exec_reset(self.email,self.otp,password)
                if response['status'] == 200:
                    self.label_notice['text'] = response['msg']
                    self.label_pw.pack_forget()
                    self.entry_pw.pack_forget()
                    self.label_cfpw.pack_forget()
                    self.entry_cfpw.pack_forget()
                    self.button_next3.pack_forget()
                else:
                    self.label_notice['text'] = response['msg']
            except:
                self.label_notice['text'] = "ERROR"
        else:
            self.label_notice['text'] = "Please entry password"
