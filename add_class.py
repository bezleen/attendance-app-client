import tkinter as tk
import cv2
import numpy as np
import os
from PIL import Image
import execute_api.add_class as ac

class AddClassPage(tk.Frame):

    def __init__(self, parent, controller, at=None, rt=None, datas=[]):
        tk.Frame.__init__(self, parent)
        self.container = parent
        self.controller = controller
        self.at = at
        self.rt = rt
        self.init_UI()


    def init_UI(self):
        label_title = tk.Label(self, text="CREATE CLASSROOM")
        label_classname = tk.Label(self, text="class's name")
        self.label_notice = tk.Label(self, text="", bg="orange")

        self.entry_classname = tk.Entry(self, width=20, bg="light yellow")


        self.button_add = tk.Button(
            self, text="ADD", command=self.add)
        self.button_add.configure(width=10, bg="orange")
   
        self.button_back = tk.Button(self, text="BACK", command=lambda: self.controller.show_frame(
            self.container,
            "ClassPage",
            self.at,
            self.rt
        ))
        self.button_back.configure(width=10, bg="orange")

        label_title.pack()

        label_classname.pack()
        self.entry_classname.pack()

        self.label_notice.pack()

        self.button_add.pack()
        # self.button_register_face.pack()
        self.button_back.pack()

    def add(self):
        #check null
        name = self.entry_classname.get()
        if not name:
            self.label_notice['text'] = "Please fill the entry"
            return
        try:
            response=ac.add_class(self.at,name)
            if response['status'] == 200:
                self.label_notice['text'] = response['msg']
            elif response['status'] == 400:
                self.label_notice['text'] = response['msg']
        except:
            self.label_notice['text'] = response['SERVER ERROR']