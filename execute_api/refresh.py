PATH_AT='access_token.txt'
PATH_RT='refresh_token.txt'


def write_token(at,rt):
    with open(PATH_AT,mode='w') as f:
        f.write(at)
    with open(PATH_RT,mode='w') as f:
        f.write(rt)

        
def read_token():
        try:
            with open(PATH_AT) as f:
                access_token=f.read()
            with open(PATH_RT) as f:
                refresh_token=f.read()
        except:
            access_token=None
            refresh_token=None
        if access_token=='' or refresh_token=='':
            access_token=None
            refresh_token=None
        return access_token, refresh_token