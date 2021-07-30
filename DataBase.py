from os import close
import sqlite3 , datetime, time
from sqlite3.dbapi2 import SQLITE_SELECT
#from object_tracker import *
#from speed_calculation import *
#from object_tracker import main
#from speed_calculation import estimateSpeed, recognize_plate

################################################################










 #   Connect to database
connection = sqlite3.connect('Data.db')

#   Create cursor
cursor = connection.cursor()

#  Create a Table           
cursor.execute('CREATE TABLE IF NOT EXISTS monitoring(DateStamp text,TimeStamp text,VRN text, Speed real, VehicleType text)')
def dynamic_entry():
    vrn = plate_num  
    speed = 50.3
    type = 'Car'
    date =  f"{datetime.datetime.now():%a, %b %d %Y }"
    time_stamp =  f"{datetime.datetime.now():%I:%M:%S %p }"
 
    cursor.execute("INSERT INTO monitoring(DateStamp,TimeStamp,VRN,Speed,VehicleType) VALUES(?,?,?,?,?)", (date,time_stamp,vrn,speed,type))

  # Commit our command
    connection.commit()

for i in range(10):
    dynamic_entry()
#   Close connection
connection.close

























#   Connect to database
connection = sqlite3.connect('Data.db')

#   Create cursor
cursor = connection.cursor()

#  Create a Table           
cursor.execute('CREATE TABLE IF NOT EXISTS monitoring(DateStamp text,TimeStamp text,VRN text, Speed real, VehicleType text)')
def dynamic_entry():
  vrn = 'LP-17410'
  speed = 50.3
  type = 'Car'
  date =  f"{datetime.datetime.now():%a, %b %d %Y }"
  time_stamp =  f"{datetime.datetime.now():%I:%M:%S %p }"
 
  cursor.execute("INSERT INTO monitoring(DateStamp,TimeStamp,VRN,Speed,VehicleType) VALUES(?,?,?,?,?)", (date,time_stamp,vrn,speed,type))

  # Commit our command
  connection.commit()

for i in range(10):
  dynamic_entry()
#   Close connection
connection.close










#######################################################################



































# #   Connect to database
# connection = sqlite3.connect('Data.db')

# #   Create cursor
# cursor = connection.cursor()


# #   Update Records
# # cursor.execute("""UPDATE monitoring SET VRN = ''
# # WHERE rowid = 10
# # """) 
# # connection.commit()



# #   Delete Record
# # cursor.execute("DELETE FROM monitoring WHERE rowid = 6")
# # connection.commit()



# #  Create a Table
 
# cursor.execute("""CREATE TABLE monitoring(
#         VRN text,
#         Datestamp text
#       )""")



# #   Insert in Table
# # cursor.execute("INSERT INTO monitoring (VRN) VALUES (''") 



# #  Insert many


# cursor.executemany("INSERT INTO monitoring(VRN, Speed) VALUES (?,?)",(plate_num, cars_list ) )



# # Query The DataBase without rowid

# cursor.execute("SELECT , * FROM monitoring")
# # cursor.fetchone()  #  fetch last item in table
# # cursor.fetchmany(3)
# items = cursor.fetchall()

# # print("Date " + "\t\tTime" + "\t\t VRN" + "\t\t Speed")
# # print("________________________________________________________")
# # for item in items:
# #     print(item[0] + " | " + item[1] + "\t| " + item[2] + "\t| " + item[3])




# #Query The DataBase with rowid

# # cursor.execute("SELECT rowid, * FROM monitoring")
# # items = cursor.fetchall()
# # print("Sr# " + "\tDate " + "\t\tTime" + "\t\tVRN" + "\tSpeed")    
# # print("________________________________________________________")
# # for item in items:    
# #     print(item)


# # Data Types in sqlite are 5
# # Null , Integer, Real , Text, Blob

# # Commit our command
# connection.commit()

# #   Close connection
# connection.close

















# ###########################################
# from os import close
# import sqlite3 , datetime
# from sqlite3.dbapi2 import SQLITE_SELECT
# from object_tracker import *
# from speed_calculation import *
# from object_tracker import main
# from speed_calculation import estimateSpeed, recognize_plate



# #   Connect to database
# connection = sqlite3.connect('Data.db')

# #   Create cursor
# cursor = connection.cursor()

# #  Create a Table
 
# cursor.execute("""CREATE TABLE IF NOT EXISTS monitoring(
#         VRN text,
#         Datestamp text
#       )""")

# cursor.executemany("INSERT INTO monitoring(VRN, Speed) VALUES (?,?)",(plate_num, cars_list ) )

# # Commit our command
# connection.commit()

# #   Close connection
# connection.close



















