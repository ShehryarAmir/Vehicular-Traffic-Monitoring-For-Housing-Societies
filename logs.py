
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog 
import os, cv2, PIL, shutil, pytesseract, time
import PIL.Image , PIL.ImageTk
from tkinter import messagebox
import datetime as dt
import time, sqlite3


def to_file(y):
    path=y
    basename = os.path.basename(path) 
    print(basename)
    os.system(' move '+path+ ' /C/User/Shehryar/Downloads/MixUp-Yolo_GUI/video.avi')
    os.system('python object_tracker.py')
    quit()
    os.remove('video.avi')

root = tk.Tk()
def to_call():
    file_path = filedialog.askopenfilename()
    to_file(file_path)

root.title("TRAFFIC MONITORING SYSTEM FOR HOUSING SOCIETIES")
HEIGHT=720       
WIDTH=1280       
canvas=tk.Canvas(root, height=HEIGHT, width=WIDTH).pack()

myButton= Button(root, text="SELECT VIDEO FILE",font="Time 15",padx=40, pady=80, bg='#fed8b1',fg='#b30059', bd=3, command= to_call).place(relx=0.05,rely=0.15,relwidth=0.3,relheight=0.05)


root.mainloop()













# import dropbox,csv,logs, time,cv2,os,sys,datetime
# from absl import app, flags, logging
# from absl.flags import FLAGS
# from threading import Thread
# from object_tracker import main

# FLAGS(sys.argv)

# flags.DEFINE_boolean("use_dropbox" , True, "your token")
# flags.DEFINE_string("dropbox_access_token", '4_CjkG2ZgzwAAAAAAAAAAbn3mxrhVLKAaUtLbGQ8yQV2l2NHz6QTzax9vPbKvO8J', "YOUR_DROPBOX_APP_ACCESS_TOKEN")
# flags.DEFINE_string('logs', './detections', 'path to output log')
# flags.DEFINE_string('csv_name', 'logs.csv', 'name of log file')

# # class logs:
# #     def __init__(self, use_dropbox, dropbox_access_token):
# #         self.use_dropbox = True
# #         self.dropbox_access_token = 'Your token'
# #     def __init__(self, output_path, csv_name):
# #         self.output_path = './detections'
# #         self.csv_name = 'log.csv'



# # check to see if the Dropbox should be used
# if FLAGS.use_dropbox:
#     # connect to dropbox and start the session authorization process
#     client = dropbox.Dropbox(FLAGS.dropbox_access_token)
#     print("[SUCCESS] dropbox account linked")



# def upload_file(tempFile, client, imageID):
#     # upload the image to Dropbox and cleanup the tempory image
#     print("[INFO] uploading {}...".format(imageID))
#     path = "/{}.jpg".format(imageID)
#     client.files_upload(open(tempFile.path, "rb").read(), path)
#     tempFile.cleanup()





# # =============================================================================
# #             # Creating CSV file
# # =============================================================================


# # with open('data.csv', 'w', newline='') as f:
# #     writer = csv.writer(f)
# #     writer.writerow([''])







# # log file
# # initialize the log file
# logFile = None
# vs = main.vid 
# time.sleep(2.0)



# # loop over the frames of the stream
# while True:
#     # grab the next frame from the stream, store the current
#     # timestamp, and store the new date
#     frame = vs.read()
#     ts = datetime.now()
#     newDate = ts.strftime("%m-%d-%y")
#     # check if the frame is None, if so, break out of the loop
#     if frame is None:
#         break
#     # if the log file has not been created or opened
#     if logFile is None:
#         # build the log file path and create/open the log file
#         logPath = os.path.join(FLAGS.logs, FLAGS.csv_name)
#         logFile = open(logPath, mode="a")
#         # set the file pointer to end of the file
#         pos = logFile.seek(0, os.SEEK_END)
#         # if we are using dropbox and this is a empty log file then
#         # write the column headings
#         if FLAGS.use_dropbox and pos == 0:
#             logFile.write("Year,Month,Day,Time,Speed (in MPH),ImageID\n")
#         # otherwise, we are not using dropbox and this is a empty log
#         # file then write the column headings
#         elif pos == 0:
#             logFile.write("Year,Month,Day,Time (in MPH),Speed\n")
#  # check if the object has not been logged
#         if not to.logged:
#             # check if the object's speed has been estimated and it
#             # is higher than the speed limit
#             if to.estimated and to.speedMPH > conf["speed_limit"]:
#                 # set the current year, month, day, and time
#                 year = ts.strftime("%Y")
#                 month = ts.strftime("%m")
#                 day = ts.strftime("%d")
#                 time = ts.strftime("%H:%M:%S")
#                 # check if dropbox is to be used to store the vehicle
#                 # image
#                 if FLAGS.use_dropbox:
#                     # initialize the image id, and the temporary file
#                     imageID = ts.strftime("%H%M%S%f")
#                     tempFile = TempFile()
#                     cv2.imwrite(tempFile.path, frame)
#                     # create a thread to upload the file to dropbox
#                     # and start it
#                     t = Thread(target=upload_file, args=(tempFile,
#                         client, imageID,))
#                     t.start()
#                     # log the event in the log file
#                     info = "{},{},{},{},{},{}\n".format(year, month,
#                         day, time, to.speedMPH, imageID)
#                     logFile.write(info)
#                 # otherwise, we are not uploading vehicle images to
#                 # dropbox
#                 else:
#                     # log the event in the log file
#                     info = "{},{},{},{},{}\n".format(year, month,
#                         day, time, to.speedMPH)
#                     logFile.write(info)
#                 # set the object has logged
#                 to.logged = True