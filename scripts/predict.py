from ast import While
import cv2
import numpy as np
import requests
import marshmallow as ma
from requests.structures import CaseInsensitiveDict
import os
from PIL import Image
import pydash as py_

# CONSTANTS
DOMAIN = 'http://14.225.254.88:5000/v1/'
# DOMAIN = 'http://localhost:5000/v1/'
UPLOAD_FOLDER = os.path.join(os.path.abspath(
    os.path.dirname(os.path.dirname(__file__))), 'src/static/uploads')


class Item(ma.Schema):
    name = ma.fields.Str()
    student_id = ma.fields.Str()
    email = ma.fields.Email()
    id = ma.fields.Str()


def get_profile(student_id):
    api_url = DOMAIN+"api/student/id/"+str(student_id)
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNjUxNDA5OTU0LCJqdGkiOiI1OThkZGY5MC00N2JmLTQwYTctYWZhZC02ZTc4NGZiZGNiMDMiLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoiNjI2ZTZhZjkxMTliMmQ5YTZiY2U0Nzk3IiwibmJmIjoxNjUxNDA5OTU0LCJleHAiOjIxNjk4MDk5NTQsIm5hbWUiOiJoaWVuZHRyYm9kb2kifQ.CGiz5sFuL32UJs9IeDUuRieg8T9gtPz5HrrnUQ-PenI"
    response = requests.get(api_url,headers=headers)
    dataresp = (response.json())['data']
    obj = Item().dump(dataresp)
    name = py_.get(obj, "name")
    student_id = py_.get(obj, "student_id")
    email = py_.get(obj, "email")
    id = py_.get(obj, "id")
    return id, name, student_id, email


face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(UPLOAD_FOLDER+'/19520229.yml')
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
            id, name, student_id, email = get_profile(student_id)
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