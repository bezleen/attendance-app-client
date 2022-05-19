import tkinter as tk
import execute_api.user_info as uif
import urllib.request
import base64
from PIL import ImageTk, Image
from io import BytesIO
import execute_api.refresh as rf
import execute_api.upload_avatar as ua
from tkinter.filedialog import askopenfile
def open_file():
    file_path = askopenfile(mode='r', filetypes=[('Image Files',['*.jpg','*.jpeg','*.png'])])
    if file_path is not None:
        pass
    return file_path
class ProfilePage(tk.Frame):

    def __init__(self, parent, controller, at=None, rt=None, datas=[]):
        tk.Frame.__init__(self, parent)
        self.container = parent
        self.controller = controller
        self.at = at
        self.rt = rt
        self.init_UI()

    def init_UI(self):
        # get information
        id, email, name, imgURL = self.get_user_info()
        # label
        label_profile = tk.Label(self, text="PROFILE")
        label_id = tk.Label(self, text="ID: "+id, width=44, bg='White', fg='Black',
                            font=('Arial', 16))
        label_name = tk.Label(self, text="NAME: "+name, width=44, bg='White', fg='Black',
                              font=('Arial', 16))
        label_email = tk.Label(self, text="EMAIL: "+email, width=44, bg='White', fg='Black',
                               font=('Arial', 16))

        label_avatar = tk.Label(self, text="Avatar")
        label_c_avatar = tk.Label(self, text="Change avatar")
        # show img from URL
        u = urllib.request.urlopen(imgURL)
        raw_data = u.read()
        u.close()
        im = Image.open(BytesIO(raw_data))
        photo = ImageTk.PhotoImage(im)
        label = tk.Label(image=photo)
        label.image = photo
        c = tk.Canvas(self, width=300, height=300)
        c.create_image(10, 0, image=photo, anchor=tk.NW)
        #button
        dlbtn = tk.Button(
            self,
            text='Choose File ',
            command=lambda: self.upload_avatar()
        )
        button_home = tk.Button(
            self, text="HOME", command=lambda: self.controller.show_frame(self.container, "HomePage", self.at, self.rt))
        button_home.configure(width=10, bg="orange")
        # show
        label_profile.pack()
        label_avatar.pack()
        c.pack()
        label_c_avatar.pack()
        dlbtn.pack()
        label_id.pack()

        label_email.pack()

        label_name.pack()
        button_home.pack()
    def get_user_info(self):
        self.check_current_token()
        try:
            response = uif.exec_user_info(self.at)
            if response['status'] == 200:
                imgURL = response['data']['avatar']
                id = response['data']['id']
                name = response['data']['name']
                email = response['data']['email']
                return id, email, name, imgURL
            else:
                return None, None, None, None
        except:
            return None, None, None, None

    def check_current_token(self):
        new_at, new_rt, status = rf.check_token(self.at, self.rt)
        if not new_at and not new_rt and not status:
            pass
        elif new_at and new_rt and not status:
            self.at = new_at
            self.rt = new_rt
        elif not new_at and not new_rt and status == 'restart':
            self.controller.show_frame(
                self.container, "StartPage", self.at, self.rt)
    def upload_avatar(self):
        self.check_current_token()
        file_path = open_file()
        response=ua.up_avatar(self.at, str(file_path.name))
        self.controller.show_frame(self.container,"ProfilePage",self.at,self.rt)