import cv2
import numpy as np
import requests
import marshmallow as ma
from requests.structures import CaseInsensitiveDict
import os
from PIL import Image

# CONSTANTS
DOMAIN = 'http://14.225.254.88:5000/v1/'
# DOMAIN = 'http://localhost:5000/v1/'
UPLOAD_FOLDER = os.path.join(os.path.abspath(
    os.path.dirname(os.path.dirname(__file__))), 'src/static/uploads')


# INPUT
class Item(ma.Schema):
    name = ma.fields.Str()
    student_id = ma.fields.Str()
    email = ma.fields.Email()

name= input("enter name: ")
student_id= input("student_id: ")
email= input("email: ")
class_oid= input("class_oid: ")


# name = "hiendtr"
# student_id = "19520229"
# email = "hiendtr@gmail.com"
# class_oid = "627004c161c3be8ceffb8a8d"

obj = {
    "name": name,
    "student_id": student_id,
    "email": email
}


# REQUESTS API
todo = Item().load(obj)
api_url = DOMAIN+"api/student"
headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNjUxNDA5OTU0LCJqdGkiOiI1OThkZGY5MC00N2JmLTQwYTctYWZhZC02ZTc4NGZiZGNiMDMiLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoiNjI2ZTZhZjkxMTliMmQ5YTZiY2U0Nzk3IiwibmJmIjoxNjUxNDA5OTU0LCJleHAiOjIxNjk4MDk5NTQsIm5hbWUiOiJoaWVuZHRyYm9kb2kifQ.CGiz5sFuL32UJs9IeDUuRieg8T9gtPz5HrrnUQ-PenI"
payload = {'class': class_oid}

response = requests.post(api_url, json=todo, headers=headers, params=payload)

# return_data = response.json()
# data = return_data['data']
# try:
#     id = data['id']
# except:
#     id = None
id=student_id

# REGISTER STUDENT FACE
if response.status_code == 200 and id:

    # GET 100 IMAGE
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
            cv2.imwrite(UPLOAD_FOLDER+"/"+id+"-"+str(index) +
                        ".jpg", gray[y: y+h, x: x+w])

        cv2.imshow('DETECTING FACE', frame)
        cv2.waitKey(1)
        if index >= 100:
            break
    cap.release()
    cv2.destroyAllWindows()

    # # TRAINING
    # recognizer = cv2.face.LBPHFaceRecognizer_create()
    # path= UPLOAD_FOLDER
    # def get_image_id(path):
    #     image_path=[]
    #     for i in os.listdir(path):
    #         image_path.append(os.join(path,i))
        
    #     faces=[]
    #     ids=[]
    #     for i in image_path:
    #         face_image=Image.open(i).convert('L')
    #         face_np= np.array(face_image,'uint8')
    #         id= i.split('-')[0].split('/')[-1]
    #         faces.append(face_np)
    #         ids.append(id)
    #         cv2.imshow('TRAINING',face_np)
    #         cv2.waitKey(10)
    #     return faces,ids
    # faces,ids=get_image_id(path)
    # recognizer.train(faces,np.array(ids))
    # recognizer.save(UPLOAD_FOLDER+"/"+id+".yml")
    # cv2.destroyAllWindows()
elif response.status_code == 400:
    print("Student is already taken!")
else:
    print('ERROR')
