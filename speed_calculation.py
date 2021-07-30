
import cv2, csv
import math,time
import numpy as np
from core.functions import *
import pytesseract
import re

from os import close
import sqlite3 , datetime
from sqlite3.dbapi2 import SQLITE_SELECT
# from object_tracker import *
# from object_tracker import main

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Shahid Umar\AppData\Local\Programs\Tesseract-OCR\tesseract'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

global speed, plate_num

def estimateSpeed(location1, location2,maxWidth, maxHeight,bbox,class_name):
    d_pixels = math.sqrt(math.pow(location2[0] - location1[0], 2) + math.pow(location2[1] - location1[1], 2))
    length_pixels_2 = math.sqrt(math.pow(bbox[0] -bbox[2], 2) + math.pow(bbox[1] - bbox[3], 2))
    length_car_pixel_2 = abs (bbox[0] -bbox[2])
    if length_car_pixel_2<50:
        
        d_pixels = math.sqrt(math.pow(location2[0] - location1[0], 2))
        if d_pixels<1:
            speed = 0.0
        else:
            alpha = length_car_pixel_2/50
        if class_name =='Car':
             car_width = 3.5*alpha
        elif class_name =='Truck':
             car_width = 4.5*alpha
        elif class_name =='Van':
             car_width = 3.5*alpha
        elif class_name =='Motorcycle':
             car_width = 2*alpha
        else:
             car_width = 4*alpha
        d_meters = d_pixels *car_width/50
    else: 
        d_pixels = math.sqrt(math.pow(location2[0] - location1[0], 2))
        if d_pixels<1:
            speed = 0.0
        else:
            if class_name =='Car':
                car_width = 3.5
            elif class_name =='Truck':
                car_width = 4.5
            elif class_name =='Van':
                car_width = 3.5
            elif class_name =='Motorcycle':
                car_width = 2
            else:
                car_width = 2
            d_meters = d_pixels *car_width/length_car_pixel_2
            # ppm = maxHeight / 50
            # ppm = 11.56
            # d_meters = d_pixels / ppm
            
            #print("d_pixels=" + str(d_pixels), "d_meters=" + str(d_meters))
    fps = 30
    
    speed = (d_meters * fps * 3.6)

    # #   Connect to database
    # connection = sqlite3.connect('Data.db')

    #             #   Create cursor
    # cursor = connection.cursor()

    #             #  Create a Table
                
    # cursor.execute("""CREATE TABLE IF NOT EXISTS monitoring(
    #                     VRN text,
    #                     Datestamp text
    #                 )""")

    # cursor.executemany("INSERT INTO monitoring(VRN) VALUES (?)",( speed ) )

    #             # Commit our command
    # connection.commit()

    #             #   Close connection
    # connection.close
    # header = ['speed']
    # with open('data.csv', 'wt', newline = '') as csvfile:
    #     my_writer = csv.writer(csvfile, delimiter = ';')
    #     my_writer.writerow(i for i in header)
    #     for j in speed:
    #         my_writer.writerow(j)
    if speed<5:
        speed = 0 

    

    return int(speed)


# function to recognize license plate numbers using Tesseract OCR
def recognize_plate(img, coords):
    # separate coordinates from box
    xmin, ymin, xmax, ymax = coords
    # get the subimage that makes up the bounded region and take an additional 5 pixels on each side
    box = img[int(ymin)-5:int(ymax)+5, int(xmin)-5:int(xmax)+5]
    # grayscale region within bounding box
    gray = cv2.cvtColor(box, cv2.COLOR_RGB2GRAY)
    # resize image to three times as large as original for better readability
    gray = cv2.resize(gray, None, fx = 3, fy = 3, interpolation = cv2.INTER_CUBIC)
    # perform gaussian blur to smoothen image
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    #cv2.imshow("Gray", gray)
    #cv2.waitKey(0)
    # threshold the image using Otsus method to preprocess for tesseract
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    #cv2.imshow("Otsu Threshold", thresh)
    #cv2.waitKey(0)
    # create rectangular kernel for dilation
    rect_kern = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    # apply dilation to make regions more clear
    dilation = cv2.dilate(thresh, rect_kern, iterations = 1)
    #cv2.imshow("Dilation", dilation)
    #cv2.waitKey(0)
    # find contours of regions of interest within license plate
    try:
        contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    except:
        ret_img, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # sort contours left-to-right
    sorted_contours = sorted(contours, key=lambda ctr:cv2.boundingRect(ctr)[0] + cv2.boundingRect(ctr)[1] * cv2.boundingRect(ctr)[0])
    # create copy of gray image
    im2 = gray.copy()
    # create blank string to hold license plate number
    plate_num = ""
    # loop through contours and find individual letters and numbers in license plate
    for cnt in sorted_contours:
        x,y,w,h = cv2.boundingRect(cnt)
        height, width = im2.shape
        # if height of box is not tall enough relative to total height then skip
        if height / float(h) > 5: continue  #6

        ratio = h / float(w)
        # if height to width ratio is less than 1.5 skip
        if ratio < 1.5: continue            

        # if width is not wide enough relative to total width then skip
        if width / float(w) > 12: continue

        area = h * w
        # if area is less than 100 pixels skip
        if area < 90: continue

        # draw the rectangle
        rect = cv2.rectangle(im2, (x,y), (x+w, y+h), (0,255,0),2)
        # grab character region of image
        roi = thresh[y-5:y+h+5, x-5:x+w+5]
        # perfrom bitwise not to flip image to black text on white background
        roi = cv2.bitwise_not(roi)
        # perform another blur on character region
        roi = cv2.medianBlur(roi, 5)
        try:
            text = pytesseract.image_to_string(roi, config='-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 8 --oem 3')
            # clean tesseract text by removing any unwanted blank spaces
            clean_text = re.sub('[\W_]+', '', text)
            plate_num += clean_text
        except: 
            text = None
    if plate_num != None:
        print("License Plate #: ", plate_num)

        
    # #   Connect to database
    # connection = sqlite3.connect('Data.db')

    #             #   Create cursor
    # cursor = connection.cursor()

    #             #  Create a Table
                
    # cursor.execute("""CREATE TABLE IF NOT EXISTS monitoring(
    #                     Datestamp text
    #                     VRN text,
    #                     Speed text,
    #                     Vehicle_Type text
    #                 )""")
    # unix = time.time()
    # date =  str(datetime.datetime.fromtimestamp(unix).strftime('%D-%M-%Y  %I:%M:%S %p'))
    # cursor.executemany("INSERT INTO monitoring(Datestamp,VRN,Speed,Vehicle_Type) VALUES (?,?,?,?)",(unix,date ,plate_num,  ) )

    #             # Commit our command
    # connection.commit()

    #             #   Close connection
    # connection.close
    #cv2.imshow("Character's Segmented", im2)
    #cv2.waitKey(0)
    return plate_num

def speed_estimation_module(frame,warped_,cars_list, track,bbox,maxWidth, maxHeight):
    cars_list[int(track.track_id),0] = int(track.track_id)
    spd = -1
    if track.track_id:
        if warped_.any():
            location_ = np.argwhere(warped_ > 1)
            location_1 = np.zeros(2)
            location_1[0] = int(np.mean(location_[:,0]))
            location_1[1] = int(np.mean(location_[:,1]))
            if cars_list[int(track.track_id),1]>0:
                if cars_list[int(track.track_id),3]>0:
    
                    if cars_list[int(track.track_id),5]%5==0 and cars_list[int(track.track_id),5]>0:
                        cars_list[int(track.track_id),1] = cars_list[int(track.track_id),3]
                        cars_list[int(track.track_id),2] = cars_list[int(track.track_id),4]
                        
                        cars_list[int(track.track_id),3] = location_1[0]
                        cars_list[int(track.track_id),4] = location_1[1]
                        
                        spd = int(estimateSpeed(cars_list[int(track.track_id),1:3], cars_list[int(track.track_id),3:5],maxWidth, maxHeight,bbox,track.get_class()))
                        cars_list[int(track.track_id),6] = spd
                        # out_boxes, out_scores, out_classes, num_boxes = bboxes
                        # for i in range(num_boxes):
                        #     if int(out_classes[i]) < 0 or int(out_classes[i]) > num_classes: continue
                        #     coor = out_boxes[i]
                        #     fontScale = 0.5
                        #     score = out_scores[i]
                        #     class_ind = int(out_classes[i])
                        #     class_name = classes[class_ind]
                        #     if class_name not in allowed_classes:
                        #         continue
                        #     else:
                        #         if read_plate:
                        #             height_ratio = int(image_h / 25)
                        #             plate_number = recognize_plate(image, coor)
                                    
                    # elif cars_list[int(track.track_id),6]>0:
                    #     cv2.putText(frame, str(cars_list[int(track.track_id),6]) ,(int(bbox[0]), int(bbox[1]-10)),0, 0.75, (255,255,255),2)
                else:
                    cars_list[int(track.track_id),3] = location_1[0]
                    cars_list[int(track.track_id),4] = location_1[1]
                    # cv2.putText(frame,  (int(bbox[0]), int(bbox[1]-10)),0, 0.75, (255,255,255),2)
                cars_list[int(track.track_id),5] = cars_list[int(track.track_id),5]+1
                    
            else:
                cars_list[int(track.track_id),1] = location_1[0]
                cars_list[int(track.track_id),2] = location_1[1]
            
            
            if cars_list[int(track.track_id),6]>0:
                cv2.putText(frame, str(cars_list[int(track.track_id),6]) + "  km/h" ,(int(bbox[0]), int(bbox[1]-10)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (128,0,0),2)
                
                #   Connect to database
                connection = sqlite3.connect('Data.db')

#   Create cursor
                cursor = connection.cursor()

#  Create a Table           
                cursor.execute('CREATE TABLE IF NOT EXISTS monitoring(DateStamp text,TimeStamp text,VRN text, Speed real, VehicleType text)')
                def dynamic_entry():
                    vrn = 'LP-17410'
                    speed = cars_list[int(track.track_id),6]
                    type = 'Car'
                    date =  f"{datetime.datetime.now():%a, %b %d %Y }"
                    time_stamp =  f"{datetime.datetime.now():%I:%M:%S %p }"
                
                    cursor.execute("INSERT INTO monitoring(DateStamp,TimeStamp,VRN,Speed,VehicleType) VALUES(?,?,?,?,?)", (date,time_stamp,vrn,speed,type))

                # Commit our command
                    connection.commit()

                #for i in range(10):
                dynamic_entry()
                #   Close connection
                connection.close


                # cv2.putText(frame, plate_number, (int(coor[0]), int(coor[1]-height_ratio)), cv2.FONT_HERSHEY_SIMPLEX, 1.25, (255,255,0), 2)
            # else:
            #     cv2.putText(frame, '-',(int(bbox[0]), int(bbox[1])),0, 0.75, (255,255,255),2)

    return cars_list, frame
# print (cars_list)
