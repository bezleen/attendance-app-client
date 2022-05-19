from requests.structures import CaseInsensitiveDict
from datetime import datetime
import json
import requests
import marshmallow as ma


PATH_AT = 'access_token.txt'
PATH_RT = 'refresh_token.txt'
PREFIX_DOMAIN = "http://14.225.254.88:5000/v1"


def write_token(at, rt):
    with open(PATH_AT, mode='w') as f:
        f.write(at)
    with open(PATH_RT, mode='w') as f:
        f.write(rt)


def read_token():
    try:
        with open(PATH_AT) as f:
            access_token = f.read()
        with open(PATH_RT) as f:
            refresh_token = f.read()
    except:
        access_token = None
        refresh_token = None
    if access_token == '' or refresh_token == '':
        access_token = None
        refresh_token = None
    return access_token, refresh_token


def check_token(access_token, refresh_token):
    url = PREFIX_DOMAIN+"/api/user/ping"
    headers = CaseInsensitiveDict()
    headers['Authorization'] = "Bearer " + access_token
    response = requests.post(url=url, headers=headers)
    try:
        response = response.json()
        # khong lam j
        if response['status'] == 200:
            at = None
            rt = None
            status = None
        else:  # get new token
            url = PREFIX_DOMAIN+"/api/user/refresh"
            headers = CaseInsensitiveDict()
            headers['Authorization'] = "Bearer " + refresh_token
            response = requests.post(url=url, headers=headers)
            # cap nhat token moi
            if response['status'] == 200:
                at = response['data']['access_token']
                rt = response['data']['refresh_token']
                status = None
                write_token(at, rt)
            # dang nhap lai
            else:
                at = None
                rt = None
                status = 'restart'
                write_token('', '')
    except:
        url = PREFIX_DOMAIN+"/api/user/refresh"
        headers = CaseInsensitiveDict()
        headers['Authorization'] = "Bearer " + refresh_token
        response = requests.post(url=url, headers=headers)
        # cap nhat token moi
        if response['status'] == 200:
            at = response['data']['access_token']
            rt = response['data']['refresh_token']
            status = None
            write_token(at, rt)
        # dang nhap lai
        else:
            at = None
            rt = None
            status = 'restart'
            write_token('', '')
    return at, rt, status
