
from requests.structures import CaseInsensitiveDict
import requests





PREFIX_DOMAIN= "http://14.225.254.88:5000/v1"
def up_avatar(access_token,img_path):
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer "+str(access_token)
    url=PREFIX_DOMAIN+"/api/user/avatar"
    files={'file':open(img_path, "rb")}
    response= requests.put(url=url,files=files,headers=headers)
    return response.json()