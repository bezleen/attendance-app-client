import tkinter as tk
import execute_api.add_student_class as astc
import cv2
import numpy as np
import os
from PIL import Image
import execute_api.refresh as rf

UPLOAD_FOLDER = os.path.join(os.path.abspath(
    os.path.dirname(os.path.dirname(__file__))), 'hello_n/static/images')

SAVE_FOLDER=os.path.join(os.path.abspath(
    os.path.dirname(os.path.dirname(__file__))), 'hello_n/static/files')

def get_image_id(path):
    image_path = []
    for i in os.listdir(path):
        image_path.append(os.path.join(path, i))

    faces = []
    ids = []
    for i in image_path:
        face_image = Image.open(i).convert('L')
        face_np = np.array(face_image, 'uint8')
        id = int(i.split('-')[0].split('/')[-1])
        faces.append(face_np)
        ids.append(id)
        # cv2.imshow('TRAINING', face_np)
        cv2.waitKey(10)
        
    return faces, ids

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
        print(UPLOAD_FOLDER)

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
        self.check_current_token()

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
                self.student_id = student_id
                self.button_register.pack_forget()
                self.button_back.pack_forget()
                self.button_register_face.pack()
                self.label_notice['text'] = response['msg']
            else:
                self.label_notice['text'] = response['msg']
        except:
            self.label_notice['text'] = "SERVER ERROR"

    def exe_register_student_face(self):
        face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        cap = cv2.VideoCapture(0)
        index = 0
        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 225, 0), 2)
                index = index+1
                cv2.imwrite(UPLOAD_FOLDER+"/"+self.student_id+"-"+str(index) +
                            ".jpg", gray[y: y+h, x: x+w])

            cv2.imshow('DETECTING FACE', frame)
            cv2.waitKey(1)
            if index >= 100:
                break
        cap.release()
        cv2.destroyAllWindows()
        self.button_register_face.pack_forget()
        self.label_notice['text'] = "Training......................."
        self.train_image()
        self.label_notice['text'] = "Done"
        self.button_back.pack()
    
    def train_image(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        faces, ids = get_image_id(UPLOAD_FOLDER)
        recognizer.train(faces, np.array(ids))
        #delete_old_files
        try:
            os.remove(SAVE_FOLDER+"/me.yml")
        except:
            pass
        recognizer.save(SAVE_FOLDER+"/me.yml")

    def done(self):
        self.check_current_token()

        pass
    def check_current_token(self):
        new_at,new_rt,status= rf.check_token(self.at,self.rt)
        if not new_at and not new_rt and not status:
            pass
        elif new_at and new_rt and not status:
            self.at = new_at
            self.rt = new_rt
        elif not new_at and not new_rt and status=='restart':
            self.controller.show_frame(self.container,"StartPage",self.at,self.rt)

