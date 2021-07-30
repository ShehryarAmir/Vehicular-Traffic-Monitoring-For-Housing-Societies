from tkinter import *
from tkinter import ttk
 # TreeView   

# style = ttk.Style()
# style.theme_use('default')
# style.configure("Treeview",
#     background = "#D3D3D3",
#     foreground = "black",
#     rowheight = 25,
#     fieldbackground = "#D3D3D3"
#    )

from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog 
import os, cv2, PIL, shutil, pytesseract, time
import PIL.Image , PIL.ImageTk
from tkinter import messagebox
import datetime as dt
import time, sqlite3


width, height = 800, 600
cap = cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

root = tk.Tk()
# root = tk.Tk()
root.bind('<Escape>', lambda e: root.quit())
#lmain = tk.Label(root)
#lmain.pack()

# def show_frame():
#     _, frame = cap.read()
#     frame = cv2.flip(frame, 1)
#     cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
#     img = PIL.Image.fromarray(cv2image)
#     imgtk = PIL.ImageTk.PhotoImage(image=img)
#     lmain.imgtk = imgtk
#     lmain.configure(image=imgtk)
#     lmain.after(10, show_frame)

# show_frame()
# root.mainloop()





def web_cam():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = PIL.Image.fromarray(cv2image)
    imgtk = PIL.ImageTk.PhotoImage(image=img)
    #lmain.imgtk = imgtk
    #lmain.configure(image=imgtk)
    #lmain.after(10, web_cam)

#def to_file(y):
   # path=y
   # basename = os.path.basename(path) 
    #print(basename)
    #os.system(' mv '+path+ ' /C/User/Shehryar/Downloads/MixUp-Yolo_GUI/video.avi')
    #os.system('python object_tracker.py')
    #quit()
   # os.remove('video.avi')

#def to_call():
   # file_path = filedialog.askopenfilename()
    #to_file(file_path)

root.title("TRAFFIC MONITORING SYSTEM FOR HOUSING SOCIETIES")
HEIGHT=720       
WIDTH=1280       
canvas=tk.Canvas(root, height=HEIGHT, width=WIDTH).pack()
mybutton = Button(root, text="OPEN CAMERA" , font="Time 15",padx=40, pady=80, bg='#b19cd9',fg='#b00059', bd=3, command= web_cam).place(relx=0.05,rely=0.21,relwidth=0.3,relheight=0.05 )
root.mainloop()



