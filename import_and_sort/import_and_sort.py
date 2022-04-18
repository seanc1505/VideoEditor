import os
import datetime
import shutil
from tkinter import filedialog
import os
from tkinter import *


# Sample Implementation 
    # file_source = "F:/DCIM/100GOPRO/"# File source
    # base_save_location = "D:/00_Videos/"# File save destination
    # importSort(file_source,base_save_location)

# Work to add;
    # 1) 
        # A location for each date as its created, folder name YYYY_MM_DD_<river>
        # Maybe show an image when the file is being created and get them to pick a file name based on that
        # Ask them if they can identify, if not ask again with new picute

def checkValidDirectory(dir):    
    if dir == "":
        root = Tk()
        dir = filedialog.askdirectory()
        root.destroy()
    elif not(os.path.exists(dir)):
        os.mkdir(dir)
    return dir

def importSort(source="",save_location=""):
    
    source = checkValidDirectory(source)
    save_location = checkValidDirectory(save_location)

    date_string_format = '%Y_%m_%d' #folder name format

    file_list = os.listdir(source)

    for file in file_list:
        if file[-4:] == ".MP4" or file[-4:] == ".mp4":
            source_file = source + file
            # create/check destination folder is the date created
            # Add a location argument in the future
            utc_created_time = os.path.getmtime(source_file)
            date_created = datetime.datetime.utcfromtimestamp(utc_created_time).strftime(date_string_format)
            file_save_location = save_location + date_created
            file_save_location = checkValidDirectory(file_save_location)
            # Rename the file to GH<name><chapter>.mp4
            if file[-7] != "_":
                chapter = "_" + file[2:4]
                updated_file_name = file[:2] + file[4:-4] +  chapter +".mp4"
            else: 
                updated_file_name = file
            new_file_location = file_save_location +"/"+ updated_file_name
            print("Moving: "+file)             
            # Move file to new location
            shutil.move(source_file, new_file_location)
        elif file[-4:] == ".JPG" or file[-4:] == ".jpg":
            pass
        else:
            # delete all non mp4 files 
            os.remove(source+file)


