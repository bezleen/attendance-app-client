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


# TRAINING
recognizer = cv2.face.LBPHFaceRecognizer_create()
path = UPLOAD_FOLDER


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
        cv2.imshow('TRAINING', face_np)
        cv2.waitKey(10)
        
    return faces, ids
    
def delete_image(path):
    image_path = []
    for i in os.listdir(path):
        image_path.append(os.path.join(path, i))
    for i in image_path:
        os.remove(i)
    return





faces, ids = get_image_id(path)
# print(faces)
recognizer.train(faces, np.array(ids))
delete_image(path)
recognizer.save(UPLOAD_FOLDER+"/"+str(ids[0])+".yml")

cv2.destroyAllWindows()
