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
    source = path
    dest = 'C:/Users/Shehryar/Downloads/MixUp-Yolo-GUI/video.mp4'
    basename = os.path.basename(path) 
    print(basename)
    print(path)
    shutil.move(source, dest, copy_function=shutil.copy2)
    # os.system(' mv '+path+ ' /C/User/Shehryar/Downloads/MixUp-Yolo_GUI/video.avi')
    os.system('python object_tracker.py')
    shutil.move(dest, source, copy_function=shutil.copy2)
    # quit()
    # os.remove('video.avi')

root = tk.Tk()
def to_call():
    file_path = filedialog.askopenfilename()
    to_file(file_path)

def web_cam():

    # define a video capture object
    vid = cv2.VideoCapture(0)
    while(True):
        
        # Capture the video frame by frame
        ret, frame = vid.read()
    
        # Display the resulting frame
        cv2.imshow('Camera', frame)
        
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

def details():       
    #global my_tree
    new= Toplevel(root)
    new.geometry("750x500")
    new.title("Details")

    # TreeView
    my_tree = ttk.Treeview(new)

    # Columns Definition and Format
    my_tree['columns'] = ("VRN",  "VehicleType", "Speed","ID", "DateStamp" ,"TimeStamp")
    my_tree.column("#0" , width=0, stretch= NO)
    my_tree.column("ID" ,anchor=CENTER , width=80)
    my_tree.column("DateStamp" ,anchor=CENTER , width=120)
    my_tree.column("TimeStamp", anchor=CENTER , width=120)
    my_tree.column("VRN", anchor=CENTER , width=120)
    my_tree.column("Speed", anchor=CENTER , width=80)
    my_tree.column("VehicleType",anchor=CENTER , width=120)

    # Headings
    my_tree.heading("#0" , text = "", anchor= W )
    my_tree.heading("ID" ,text= "ID", anchor=CENTER )
    my_tree.heading("DateStamp" ,text = "Date", anchor=CENTER)
    my_tree.heading("TimeStamp",text="Time", anchor=CENTER )
    my_tree.heading("VRN", text="VRN",anchor=CENTER )
    my_tree.heading("Speed", text="Speed (KM/h)",anchor=CENTER )
    my_tree.heading("VehicleType",text="Vehicle Type",anchor=CENTER )


    def query_database():
	# Create a database or connect to one that exists
	    conn = sqlite3.connect('data.db')

	# Create a cursor instance
	    c = conn.cursor()

	    c.execute("SELECT rowid, * FROM monitoring")
	    records = c.fetchall()
	
	# Add our data to the screen
	    global count
	    count = 0

	    for record in records:
		    if count % 2 == 0:
			    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[3], record[5], record[4], record[0], record[1], record[2]), tags=('evenrow',))
		    else:
			    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[3], record[5], record[4], record[0], record[1], record[2]), tags=('oddrow',))
		# increment counter
		    count += 1


	# Commit changes
	    conn.commit()

	# Close our connection
	    conn.close()


     
    style = ttk.Style(new)
    style.theme_use('default')
    style.configure("Treeview",background=  "white",
    foreground = "black",
    rowheight = 25,
    fieldbackground = "#D3D3D3"
    )
#347083, e9692c
    style.map('Treeview', background = [('selected',"#4A235A")])
    tree_frame = Frame(new)
    tree_frame.pack(pady = 10)

    tree_scroll = Scrollbar(tree_frame)
    # tree_scroll.pack(side=RIGHT , fill=Y)

    # my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode= "extended")
    # my_tree.pack()

    tree_scroll.config(command=my_tree.yview)
 #"23, June 2021", "11:39:54 PM"

    # data = [["23, June 2021",  "11:39:54 PM" ,"lp-1245",  "50" , "Car"  ],
    #         ["23, June 2021",  "1:09:54 AM" ,"Ap-585",  "55" , "Car"  ],
    #         ["23, June 2021",  "5:01:54 PM" ,"lz-1455",  "40" , "Van"  ],
    #         ["23, June 2021",  "10:45:54 PM" ,"AJ-1289",  "30" , "Truck"  ],
    #         ["23, June 2021",  "11:39:54 PM" ,"lp-1245",  "50" , "Car"  ],
    #         ["23, June 2021",  "1:09:54 AM" ,"Ap-585",  "55" , "Car"  ],
    #         ["23, June 2021",  "5:01:54 PM" ,"lz-1455",  "40" , "Van"  ],
    #         ["23, June 2021",  "10:45:54 PM" ,"AJ-1289",  "30" , "Truck"  ],
    #         ["23, June 2021",  "1:09:54 AM" ,"Ap-585",  "55" , "Car"  ],
    #         ["23, June 2021",  "5:01:54 PM" ,"lz-1455",  "40" , "Van"  ],
    #         ["23, June 2021",  "10:45:54 PM" ,"AJ-1289",  "30" , "Truck"  ],
    #         ["23, June 2021",  "11:39:54 PM" ,"lp-1245",  "50" , "Car"  ],
    #         ["23, June 2021",  "1:09:54 AM" ,"Ap-585",  "55" , "Car"  ],
    #         ["23, June 2021",  "5:01:54 PM" ,"lz-1455",  "40" , "Van"  ]
    
    # ]

    my_tree.tag_configure('oddrow', foreground="white")
    my_tree.tag_configure('evenrow', background="#d2b2e5")
    # global count
    # count = 0
    # for records in data:
    #     if count % 2 == 0:
    #         my_tree.insert(parent= '', index='end', iid=count, text="", values = (records[0], records[1],records[2],records[3],records[4]), tags = ('evenrow',))
    #     else:
    #         my_tree.insert(parent= '', index='end', iid=count, text="", values = (records[0], records[1],records[2],records[3],records[4]), tags = ('oddrow',))
    #     count += 1

   
    def remove_one():
        x = my_tree.selection()[0]
        my_tree.delete(x)

    
 

    # Add Record Entry Boxes
    data_frame = LabelFrame(new, text="Record")
    data_frame.pack(fill="x", expand="yes", padx=20)

    vrn_label = Label(data_frame, text="VRN")
    vrn_label.grid(row=0, column=0, padx=10, pady=10)
    vrn_entry = Entry(data_frame)
    vrn_entry.grid(row=0, column=1, padx=10, pady=10)

    vt_label = Label(data_frame, text="Vehicle Type")
    vt_label.grid(row=0, column=2, padx=10, pady=10)
    vt_entry = Entry(data_frame)
    vt_entry.grid(row=0, column=3, padx=10, pady=10)

    id_label = Label(data_frame, text="ID")
    id_label.grid(row=0, column=4, padx=10, pady=10)
    id_entry = Entry(data_frame)
    id_entry.grid(row=0, column=5, padx=10, pady=10)

    
    # time_label = Label(data_frame, text="Time")
    # time_label.grid(row=1, column=0, padx=10, pady=20)
    time_entry = Entry(data_frame)
    # time_entry.grid(row=1, column=1, padx=10, pady=20)

    
    # date_label = Label(data_frame, text="Date")
    # date_label.grid(row=1, column=2, padx=10, pady=20)
    date_entry = Entry(data_frame)
    # date_entry.grid(row=1, column=3, padx=10, pady=20)

    
    # speed_label = Label(data_frame, text="Speed")
    # speed_label.grid(row=1, column=4, padx=10, pady=20)
    speed_entry = Entry(data_frame)
    # speed_entry.grid(row=1, column=5, padx=10, pady=20)



    # Clear entry boxes
    def clear_entries():
        # Clear entry boxes
        vrn_entry.delete(0, END)
        vt_entry.delete(0, END)
        id_entry.delete(0, END)
        # speed_entry.delete(0, END)
        # date_entry.delete(0, END)
        # time_entry.delete(0, END)
       

    # Select Record
    def select_record(e):
        # Clear entry boxes
        vrn_entry.delete(0, END)
        vt_entry.delete(0, END)
        id_entry.delete(0, END)
        time_entry.delete(0, END)
	    #date_entry.delete(0, END)
	    #speed_entry.delete(0, END)
        
        # Grab record Number
        selected = my_tree.focus()
        # Grab record values
        values = my_tree.item(selected, 'values')

        # outpus to entry boxes
        vrn_entry.insert(0, values[0])
        vt_entry.insert(0, values[1])
        id_entry.insert(0, values[3]) 
        date_entry.insert(0, values[4]) 
        time_entry.insert(0, values[5]) 
        speed_entry.insert(0, values[2]) 
        
        
# Update record
    def update_record():
	# Grab the record number
        selected = my_tree.focus()
        # Update record
        my_tree.item(selected, text="", values=(vrn_entry.get(), vt_entry.get(), speed_entry.get(), id_entry.get(), date_entry.get(), time_entry.get()))

        # Clear entry boxes
        vrn_entry.delete(0, END)
        vt_entry.delete(0, END)
        id_entry.delete(0,END)
        date_entry.delete(0,END)
        speed_entry.delete(0,END)
        time_entry.delete(0,END)
        
        
    #   Data
    #my_tree.insert(parent= '', index='end', iid=0, text="", values = ("23,June","1Pm","LP-1458",84, "Car"))

    #   Child
    #my_tree.insert(parent= '0', index='end', iid=1, text="Child", values = ("24,June","3Pm","LP-1458",80, "Car"))


    button_frame = LabelFrame(new, text="Commands")
    button_frame.pack(fill="x", expand="yes" , padx=20)

    remove_one_button = Button(button_frame , text= "Remove Entry", command= remove_one )
    remove_one_button.grid(row=0, column=4, padx=10, pady=10)

    update_button = Button(button_frame, text="Update Record", command=update_record)
    update_button.grid(row=0, column=0, padx=10, pady=10)

    select_record_button = Button(button_frame, text="Clear Entry Boxes", command=clear_entries)
    select_record_button.grid(row=0, column=7, padx=10, pady=10)
    
    # Bind the treeview
    my_tree.bind("<ButtonRelease-1>", select_record)
    
    
    
    my_tree.pack()
# Run to pull data from database on start
    query_database()
def clock():
    timer = str(time.strftime("%I:%M:%S %p"))
    my_time.config(text = timer)
    my_time.after(1000, clock)

def Date():
    date = str(time.strftime("%I:%M:%S %p"))
    my_date.config(text = date)
    my_date.after(8.64*10**7, clock)


root.title("TRAFFIC MONITORING SYSTEM FOR HOUSING SOCIETIES")
HEIGHT=720       
WIDTH=1280       
canvas=tk.Canvas(root, height=HEIGHT, width=WIDTH).pack()


# self.canvas = tk.Canvas(self.window, width = self.vid.width, height = self.vid.height)
# self.canvas.grid(row=1,column=3,rowspan=10,columnspan=5,sticky=tk.N)


background_image=tk.PhotoImage(file='3c.png')
background_label= tk.Label(root, image=background_image)
background_label.place(x=0,y=0.5)

background_image2=tk.PhotoImage(file='8c.png')
background_label2= tk.Label(root, image=background_image2)
background_label2.place(relx=0.0,rely=0.35 )


myButton= Button(root, text="SELECT VIDEO FILE",font="Time 15",padx=40, pady=80, bg='#fed8b1',fg='#b30059', bd=3, command= to_call).place(relx=0.05,rely=0.15,relwidth=0.3,relheight=0.05)
mybutton = Button(root, text="OPEN CAMERA" , font="Time 15",padx=40, pady=80, bg='#b19cd9',fg='#b00059', bd=3, command= web_cam).place(relx=0.05,rely=0.21,relwidth=0.3,relheight=0.05 )
mybutton = Button(root, text="Details" , font="Time 15",padx=40, pady=80, bg='#800000',fg='#FFFFFF', bd=3, command= details).place(relx=0.05,rely=0.27,relwidth=0.3,relheight=0.05 )

tk.Label(root,relief="groove", fg="white",bg="#0875B7", text="Time : ").place(relx=0.85,rely=0.43,relwidth=0.03,relheight=0.05)
my_time = tk.Label(root,relief="groove", fg="BLUE",bg="Lightblue", text=f"{dt.datetime.now():%I:%M:%S %p}")
my_time.place(relx=0.88,rely=0.43,relwidth=0.1,relheight=0.05)
tk.Label(root,relief="groove", fg="white",bg="#0875B7", text="Date : ").place(relx=0.70,rely=0.43,relwidth=0.03,relheight=0.05)
my_date = tk.Label(root,relief="groove", fg="Blue",bg="Lightblue", text=f"{dt.datetime.now():%a, %b %d %Y}")
my_date.place(relx=0.73,rely=0.43,relwidth=0.1,relheight=0.05)
tk.Label(root,relief="groove", fg="RED",bg="#ffcccb", text="VRN : ").place(relx=0.70,rely=0.50,relwidth=0.1,relheight=0.05)
tk.Label(root,relief="groove", text="").place(relx=0.75,rely=0.56,relwidth=0.15,relheight=0.08)
tk.Label(root,relief="groove", fg="Purple",bg="#CBC3E3", text="Speed : ").place(relx=0.70,rely=0.65,relwidth=0.1,relheight=0.05)
tk.Label(root,relief="groove", text="").place(relx=0.75,rely=0.72,relwidth=0.2,relheight=0.2)

clock()


root.mainloop()