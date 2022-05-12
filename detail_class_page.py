import tkinter as tk
import execute_api.list_class as lc
import execute_api.list_attendance as la
import execute_api.get_student_info as gsti
import cv2
import numpy as np
import os
from PIL import Image

SAVE_FOLDER = os.path.join(os.path.abspath(
    os.path.dirname(os.path.dirname(__file__))), 'hello_n/static/files')


def get_profile(access_token, student_id):
    try:
        response = gsti.get_student_info(access_token, student_id)
        if response['status'] == 200:
            email = response['data']['email']
            id = response['data']['id']
            name = response['data']['name']
            student_id = response['data']['student_id']
            return id, name, student_id, email
        else:
            return None, None, None, None
    except:
        return None, None, None, None


class DetailClassPage(tk.Frame):

    def __init__(self, parent, controller, at=None, rt=None, datas=[]):
        tk.Frame.__init__(self, parent)
        self.container = parent
        self.controller = controller
        self.at = at
        self.rt = rt
        self.datas = datas
        self.class_id = datas[0]['class_id']
        self.class_datas = []
        self.init_UI()
        self.draw_table()

        self.oid = ''
        self.email = ''
        self.student_id = ''
        self.name = ''

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
            self, text="NOT ABSENT", command=self.list_attendance_attendance)
        button_attendance.configure(width=10, bg="lightblue")

        button_add_student = tk.Button(
            self, text="ADD STUDENT", command=lambda: self.controller.show_frame(
                self.container,
                "AddStudentClassPage",
                self.at,
                self.rt,
                [{"class_id": self.class_id}]
            )
        )
        button_add_student.configure(width=10, bg="orange")

        button_take_attendance = tk.Button(
            self, text="TAKE ATTENDANCE", command=self.take_attendance)
        button_take_attendance.configure(width=10, bg="orange")

        # button_home.pack()
        # button_all.pack()
        # button_absent.pack()
        # button_attendance.pack()
        # self.label_date.pack()
        # self.entry_date.pack()
        # self.label_notice.pack()

        button_home.grid(row=0, column=0, sticky=tk.NSEW)
        button_take_attendance.grid(row=0, column=1, sticky=tk.NSEW)
        button_add_student.grid(row=0, column=2, sticky=tk.NSEW)
        button_all.grid(row=1, column=0, sticky=tk.NSEW)
        button_absent.grid(row=1, column=1, sticky=tk.NSEW)
        button_attendance.grid(row=1, column=2, sticky=tk.NSEW)
        self.label_date.grid(row=4, column=1, sticky=tk.NSEW)
        self.entry_date.grid(row=5, column=1, sticky=tk.NSEW)
        self.label_notice.grid(row=6, column=1)

    def list_attendance_all(self):
        self.label_notice['text'] = ""
        # check date
        state = "all"
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
                # print(response['data'])
                self.del_table()
                self.class_datas = response['data']
                print(self.class_datas)
                self.draw_table()
        except:
            pass

    def list_attendance_absent(self):
        self.label_notice['text'] = ""
        # check date
        state = "absent"
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
                # print(response['data'])
                self.del_table()
                self.class_datas = response['data']
                print(self.class_datas)
                self.draw_table()
        except:
            pass

    def list_attendance_attendance(self):
        self.label_notice['text'] = ""
        # check date
        state = "attendance"
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
                # print(response['data'])
                self.del_table()
                self.class_datas = response['data']
                print(self.class_datas)
                self.draw_table()
        except:
            pass

    def del_table(self):
        datas = self.class_datas
        height = len(datas)
        width = 3
        for i in range(8, 8+height):  # Rows
            for j in range(width):  # Columns
                self.nametowidget(str(i-8)+"-"+str(j)).destroy()

    def draw_table(self):
        columns = ["Email", "Name", "Student Id"]
        for i in range(len(columns)):
            b = tk.Entry(self, width=44, bg='LightSteelBlue', fg='Black',
                         font=('Arial', 16, 'bold'))
            b.grid(row=7, column=i)
            b.insert(tk.END, columns[i])
        datas = self.class_datas
        height = len(datas)
        width = 3
        for i in range(8, 8+height):  # Rows
            for j in range(width):  # Columns
                b = tk.Entry(self, text="", name=str(i-8)+"-"+str(j), width=44, bg='White', fg='Black',
                             font=('Arial', 16))
                b.grid(row=i, column=j)
                if j == 0:
                    b.insert(tk.END, datas[i-8]['email'])
                elif j == 1:
                    b.insert(tk.END, datas[i-8]['name'])
                elif j == 2:
                    b.insert(tk.END, datas[i-8]['student_id'])

    def take_attendance(self):
        face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(SAVE_FOLDER+'/me.yml')
        cap = cv2.VideoCapture(0)
        fontface = cv2.FONT_HERSHEY_SIMPLEX
        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 225, 0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                student_id, confidence = recognizer.predict(roi_gray)
                if confidence < 40:
                    id, name, student_id, email = get_profile(self.at,student_id)
                    self.oid = id
                    self.email = email
                    self.student_id = student_id
                    self.name = name
                    if id and name and email and student_id:
                        cv2.putText(frame, name, (x+10, y+h+30),
                                    fontface, 1, (0, 255, 0), 2)
                        cv2.putText(frame, student_id, (x+10, y+h+60),
                                    fontface, 1, (0, 255, 0), 2)
                        cv2.putText(frame, email, (x+10, y+h+90),
                                    fontface, 1, (0, 255, 0), 2)
                else:
                    cv2.putText(frame, "Unknow", (x+10, h+h+30),
                                fontface, 1, (0, 0, 225), 2)
            cv2.imshow('DETECTING FACE', frame)
            if cv2.waitKey(1) == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
        if self.oid and self.name and self.student_id and self.email:
            self.controller.show_frame(
                self.container,
                "TakeAttendancePage",
                self.at,
                self.rt,
                [
                    {
                        "class_id":self.class_id,
                        "student_oid":self.oid,
                        "name":self.name,
                        "email":self.email,
                        "student_id": self.student_id
                    }
                ]
            )
        else:
            return

