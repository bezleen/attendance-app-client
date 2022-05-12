from requests.structures import CaseInsensitiveDict
from datetime import datetime
import json
import requests
import marshmallow as ma


PREFIX_DOMAIN= "http://14.225.254.88:5000/v1"
def get_student_info(access_token,student_id):
    url=PREFIX_DOMAIN+"/api/student/id/"+str(student_id)
    headers = CaseInsensitiveDict()
    headers['Authorization']="Bearer "+ access_token
    response= requests.get(url=url,headers=headers)
    return response.json()
