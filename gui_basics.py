from re import sub
import tkinter as tk
from tkinter.constants import END, NE
from tkinter import filedialog
from typing import Text
from datetime import date, datetime
from PIL import ImageTk, Image
import moviepy  
from moviepy.editor import *
import math

from moviepy.video.compositing.concatenate import concatenate_videoclips

class InitialWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # instantiate variables
        self.number_of_subclips = 0
        self.athlete_name="Athlete"
        self.session_type = "Flatwater"
        self.source_video_name = "Select clip"
        self.export_video_date = datetime.today().strftime('%Y_%m_%d')
        self.export_video_date = self.export_video_date[2:]
        self.export_video_name = self.export_video_date + "_undefined"
        self.source_video_clip = "undefined"
        self.source_video_duration = "Select clip"
        self.source_video_duration_opening_frame = "Select clip"
        self.subclip_dict_list_label_string = "Subclip List: \n"
        self.subclip_dict_list = []
        self.subclip_list = []
        
        self.define_gui_components()
        self.video_date_entry.insert(0, self.export_video_date)
        self.session_type_entry.insert(0, self.session_type)

        # Export Name Set
        self.export_video_name_button = tk.Button(self.export_video_details_frame, text="Export name Set", command=self.on_export_video_name_button)
        # Close button box
        self.close_button = tk.Button(self, text="Close",background="orange", command=  self.on_close_button)
        # Tutorial Button 
        self.tutorial_button = tk.Button(self,text="Need help? \nTutorial",background="orange" ,command=self.on_tutorial_button)
        # New Subclip Button
        self.new_subclip_button = tk.Button(self.new_subclip_frame,text="New Subclip",command=self.on_new_subclip_button)
        # New source video button
        self.new_source_video_button = tk.Button(self.source_video_details_frame, text="New source video",background="green",font='Helvetica 12 bold', command=self.on_new_source_video_button)
        # Export clips Button 
        self.export_video_button = tk.Button(self.new_subclip_frame,text="Export the videos", command= self.on_export_video_button)
       
        
        self.place_gui_components()
        
        

    def define_gui_components(self):
        # Opening Label
        self.title_greeting_label = tk.Label(text="Video Editing software V1")
        # Export video name details frame
        self.export_video_details_frame = tk.Frame(relief=tk.RIDGE,borderwidth=10)
        # Athlete name
        self.athlete_name_frame = tk.Frame(self.export_video_details_frame,relief=tk.RIDGE,borderwidth=5,width=150,height=75)
        self.athlete_name_label= tk.Label(self.athlete_name_frame,text="Athlete Name: ")
        self.athlete_name_entry = tk.Entry(self.athlete_name_frame)
        # Date
        self.video_date_frame = tk.Frame(self.export_video_details_frame,relief=tk.RIDGE,borderwidth=5,width=150,height=75)
        self.video_date_label= tk.Label(self.video_date_frame,text="Date: ")
        self.video_date_entry = tk.Entry(self.video_date_frame)
        
        # Session type
        self.session_type_frame = tk.Frame(self.export_video_details_frame,relief=tk.RIDGE,borderwidth=5,width=150,height=75)
        self.session_type_label= tk.Label(self.session_type_frame,text="Session type: ")
        self.session_type_entry = tk.Entry(self.session_type_frame)
        # Subclip frame 
        self.new_subclip_frame = tk.Frame(self,relief=tk.RIDGE,borderwidth=5)
        self.subclip_dict_list_label = tk.Label(self.new_subclip_frame, text= self.subclip_dict_list_label_string)
        # Export video name label
        self.export_video_name_label = tk.Label(self.export_video_details_frame,text = "Video Name: " +self.export_video_name)
        # Source video frame
        self.source_video_details_frame = tk.Frame(relief=tk.RIDGE,borderwidth=5,width=150,height=150)
        self.source_video_name_label = tk.Label(self.source_video_details_frame,text = self.source_video_name,borderwidth=5)
        self.video_name_label = tk.Label(self.source_video_details_frame,text = "Video name:",borderwidth=5)
        self.source_video_duration_label = tk.Label(self.source_video_details_frame,text = self.source_video_duration,borderwidth=5)
        self.video_duration_label = tk.Label(self.source_video_details_frame,text = "Video duration:",borderwidth=5)
        self.source_video_duration_opening_frame_label = tk.Label(self.source_video_details_frame,text = "Select Source video")



    def place_gui_components(self):
        # Opening Label
        self.title_greeting_label.grid(row=0,column=0)
        # Export video name details frame
        self.export_video_details_frame.grid(row=1,column=0,columnspan=6)
        # subclip frame
        self.new_subclip_frame.grid(row=2,column=1,sticky="NW")
        self.subclip_dict_list_label.grid(row=1,column=0)
        self.export_video_button.grid(row = 2,column = 0)
        # Athlete name
        self.athlete_name_frame.grid(row=0,column=1)
        self.athlete_name_label.grid(row = 0,column = 0)
        self.athlete_name_entry.grid(row = 0,column = 1)
        # Date
        self.video_date_label.grid(row = 0,column = 0)
        self.video_date_entry.grid(row = 0,column = 1)
        self.video_date_frame.grid(row=0,column=0)
        
        # Session type
        self.session_type_label.grid(row = 0,column = 0)
        self.session_type_entry.grid(row = 0,column = 1)
        self.session_type_frame.grid(row=0,column=3)
        
        # Buttons
        self.export_video_name_button.grid(row = 1,column = 0,columnspan=2)
        self.tutorial_button.grid(row=0,column=1)
        self.new_subclip_button.grid(row=0,column=0,sticky="NW")
        self.new_source_video_button.grid(row=0,column=0)
        self.close_button.grid(row=5,column=1)
        
        # Export video name label
        self.export_video_name_label.grid(row=1,column=3)
        
        # Source video frame
        self.video_name_label.grid(row=1,column=0)
        self.source_video_name_label.grid(row=1,column=1)
        self.video_duration_label.grid(row=2,column=0)
        self.source_video_duration_label.grid(row=2,column=1)
        self.source_video_duration_opening_frame_label.grid(row=3,column=0)
        self.source_video_details_frame.grid(row=2,column=0,sticky="NW")

    def on_close_button(self):
        self.destroy()


    def on_new_source_video_button(self):
        # Find source clip file name
        self.source_video_name = filedialog.askopenfilename()
        if len(self.source_video_name) >50:
            length = int(math.floor(len(self.source_video_name)/2))
            first_half = self.source_video_name[:(length)]
            second_half = self.source_video_name[(length):]
            self.source_video_name_label.config(text=first_half + "\n"+second_half)
        else:
            self.source_video_name_label.config(text= self.source_video_name)
        # find source clip
        self.source_video_clip =  moviepy.VideoFileClip(self.source_video_name)
        # calc duration of source clip
        self.source_video_duration = self.source_video_clip.duration
        self.source_video_duration_label.config(text=self.source_video_duration)
        # Show first frame
        self.source_video_image_array = self.source_video_clip.get_frame(0) 
        self.source_video_image_location = Image.fromarray(self.source_video_image_array)
        self.source_video_image_resized = self.source_video_image_location.resize((150,80))
        self.source_video_image = ImageTk.PhotoImage(self.source_video_image_resized)
        self.source_video_duration_opening_frame_label.config(image=self.source_video_image)
        self.source_video_duration_opening_frame_label.image = self.source_video_image
        # Perform find file things
        self.new_source_video_button.config(text="New Source video",bg="green")

    def on_export_video_name_button(self):
        self.athlete_name = self.athlete_name_entry.get()
        self.export_video_date = self.video_date_entry.get()
        self.session_type = self.session_type_entry.get()
        self.export_video_name = self.export_video_date+ "_" + self.session_type + "_" + self.athlete_name 
        self.export_video_name_label.config(text="Video Name: " +self.export_video_name)

    def on_export_video_button(self):
        print("lets Export")
        if self.subclip_dict_list == []:
            self.export_video_button.config(text="Enter min 1 subclip",bg ="red")
            self.new_subclip_button.config(bg="red")

        else:
            for subclip in self.subclip_dict_list:
                current_subclip = self.source_video_clip.subclip(subclip["start time"], subclip["end time"])
                self.subclip_list.append(current_subclip)
            print(self.subclip_list)
            self.final_clip = concatenate_videoclips(self.subclip_list)
            self.final_clip.write_videofile(self.export_video_name+".mp4")


    def on_tutorial_button(self):
        print("Display Tutorial")


    def on_subclip_close(self):
        for subclip in self.subclip_dict_list:
            current_sublist = subclip
            if  ("Clip number: " + subclip["subclip name"]) not in self.subclip_dict_list_label_string:
                self.subclip_dict_list_label_string += "Clip number: " + subclip["subclip name"]
                self.subclip_dict_list_label_string += " strt: " + str(subclip["start time"])
                self.subclip_dict_list_label_string += " end: " + str(subclip["end time"]) + "\n"
        self.subclip_dict_list_label.config(text=self.subclip_dict_list_label_string)
        print(self.subclip_list)

     
    def on_new_subclip_button(self):
        if self.source_video_clip == "undefined":
            self.new_source_video_button.config(text="Set Source video first",bg="red")
            self.new_subclip_button.config(text="Set Source video first",bg="red")
        else:
            
            self.new_subclip_button.config(text="Subclip video",bg="green")
        # New source video button
            self.new_source_video_button = tk.Button(self.source_video_details_frame, text="New source video",background="green",font='Helvetica 12 bold', command=self.on_new_source_video_button)
        
            self.subclip = SubclipWindow(source_window=self)
            # subclip.focus
            # subclip.show
            self.subclip.geometry("500x400")
            # subclip.number_of_subclips =self.number_of_subclips
            self.subclip.mainloop()







class SubclipWindow(tk.Toplevel):
    def __init__(self,source_window):
        tk.Toplevel.__init__(self,source_window)
        
        # Variable set up
        self.number_of_subclips = source_window.number_of_subclips
        self.source_video = source_window.source_video_clip
        self.subclip_name = "" 
        self.time_calculated = False
        self.clip_time = source_window.source_video_duration
        self.time_valid = False
        self.subclip_details_dict = {}
    
        # Time Entry-Frame
        self.time_entry_frame = tk.Frame(self,relief=tk.RIDGE,borderwidth=5)
        self.define_subclip_gui_components()
        # Calculate time button
        self.time_entry_button = tk.Button(self.time_entry_frame, text="Calculate time", command= self.on_time_entry_button)
        # Reset time button
        self.time_entry_reset_button = tk.Button(self.time_entry_frame, text="Reset Times", command= self.on_time_entry_reset_button)
        # Create Subclip Button
        self.create_subclip_button = tk.Button(self.subclip_details_frame, text="Create Subclip", command=lambda: self.on_create_subclip_button(source_window))
        # Close button
        self.close_subclip_button = tk.Button(self, text="Done",background="orange", command=lambda: self.on_close_subclip_button(source_window))

        self.place_subclip_gui_components()
        self.time_entry_frame.grid(row=1,column=0,columnspan=4)  
    
    def on_close_subclip_button(self,source_window):
        source_window.number_of_subclips = self.number_of_subclips
        source_window.on_subclip_close()
        self.destroy()

    def define_subclip_gui_components(self):      
        self.subclip_info_label = tk.Label(self,text="Please Enter subclip information")
        # start time
        self.start_time_frame = tk.Frame(self.time_entry_frame,relief=tk.RIDGE,borderwidth=1)
        self.start_time_label = tk.Label(self.start_time_frame,text="Start time")
        self.start_time_entry_min = tk.Text(self.start_time_frame,width=3,height=1)
        self.start_time_label_min = tk.Label(self.start_time_frame,text="min")
        self.start_time_entry_sec = tk.Text(self.start_time_frame,width=3,height=1)
        self.start_time_label_sec = tk.Label(self.start_time_frame,text="sec")
        # Duration
        self.duration_time_frame = tk.Frame(self.time_entry_frame,relief=tk.RIDGE,borderwidth=1)    
        self.duration_time_label = tk.Label(self.duration_time_frame,text="Clip duration")
        self.duration_time_entry_min = tk.Text(self.duration_time_frame,width=3,height=1)
        self.duration_time_label_min = tk.Label(self.duration_time_frame,text="min")
        self.duration_time_entry_sec = tk.Text(self.duration_time_frame,width=3,height=1)
        self.duration_time_label_sec = tk.Label(self.duration_time_frame,text="sec")
        # End time
        self.end_time_frame = tk.Frame(self.time_entry_frame,relief=tk.RIDGE,borderwidth=1)
        self.end_time_label = tk.Label(self.end_time_frame,text="End time")
        self.end_time_entry_min = tk.Text(self.end_time_frame,width=3,height=1)
        self.end_time_label_min = tk.Label(self.end_time_frame,text="min")
        self.end_time_entry_sec = tk.Text(self.end_time_frame,width=3,height=1)
        self.end_time_label_sec = tk.Label(self.end_time_frame,text="sec")
        # Start and end frame labels
        self.start_frame_label = tk.Label(self, text="Start frame")
        self.end_frame_label = tk.Label(self, text="End frame")
        # Subclip number section
        self.subclip_details_frame = tk.Frame(self,relief=tk.RIDGE,borderwidth=5)
        self.clip_number_label = tk.Label(self.subclip_details_frame,text="Current Subclip number")
        self.clip_number_entry = tk.Entry(self.subclip_details_frame)

        self.subclip_details_label_text = "Enter Subclip"
        self.subclip_details_label = tk.Label(self,text = self.subclip_details_label_text)

    def place_subclip_gui_components(self):
        # subclip info
        self.subclip_info_label.grid(row=0,column=0)   
        # start time
        self.start_time_label.grid(row= 0,column=0,columnspan=4)
        self.start_time_entry_min.grid(row= 1,column=0)
        self.start_time_entry_min.insert("1.0","0")
        self.start_time_label_min.grid(row= 1,column=1)
        self.start_time_entry_sec.grid(row= 1,column=2)
        self.start_time_entry_sec.insert("1.0","0")
        self.start_time_label_sec.grid(row= 1,column=3)
        self.start_time_frame.grid(row=0,column=0)
        # duration time
        self.duration_time_label.grid(row= 0,column=4,columnspan=4)
        self.duration_time_entry_min.grid(row= 1,column=4)
        self.duration_time_entry_min.insert("1.0","0")
        self.duration_time_label_min.grid(row= 1,column=5)
        self.duration_time_entry_sec.grid(row= 1,column=6)
        self.duration_time_entry_sec.insert("1.0","0")
        self.duration_time_label_sec.grid(row= 1,column=7)
        self.duration_time_frame.grid(row=0,column=1)
        # end time
        self.end_time_label.grid(row= 0,column=8,columnspan=4)
        self.end_time_entry_min.grid(row= 1,column=8)
        self.end_time_entry_min.insert("1.0","0")
        self.end_time_label_min.grid(row= 1,column=9)
        self.end_time_entry_sec.grid(row= 1,column=10)
        self.end_time_entry_sec.insert("1.0","0")
        self.end_time_label_sec.grid(row= 1,column=11)
        self.end_time_frame.grid(row=0,column=2)     
        # Buttons
        self.time_entry_button.grid(row=2,column=0,columnspan=2)   
        self.time_entry_reset_button.grid(row=2,column=2)
        # Start and end frame labels
        self.start_frame_label.grid(row= 2,column=0)
        self.end_frame_label.grid(row= 2,column=3)
        # Subclip number
        self.clip_number_entry.grid(row=1,column=0)
        self.clip_number_label.grid(row=0,column=0)
        self.clip_number_entry.insert(0,str(self.number_of_subclips+1))
        self.create_subclip_button.grid(row=2,column=0)
        self.subclip_details_frame.grid(row=2,column=1)     
        # Subclip details label
        self.subclip_details_label.grid(row=4,column=0,columnspan=2)
        
        # Close button
        self.close_subclip_button.grid(row=5,column=0,columnspan=4)



    def on_time_entry_reset_button(self):
        self.subclip_info_label.config(text="Please Enter subclip information" ,background="SystemButtonFace")
        self.delete_time_entries()
        self.end_time_entry_min.insert("1.0","0")
        self.end_time_entry_sec.insert("1.0","0")
        self.start_time_entry_min.insert("1.0","0")
        self.start_time_entry_sec.insert("1.0","0")
        self.duration_time_entry_min.insert("1.0","0")
        self.duration_time_entry_sec.insert("1.0","0")
        
    def on_time_entry_button(self):
        # when button is pressed get the data from time entry widgets
        self.start_time = (float(self.start_time_entry_min.get('1.0',"end-1c"))*60)+ float(self.start_time_entry_sec.get('1.0',"end-1c"))
        self.duration = (float(self.duration_time_entry_min.get('1.0',"end-1c"))*60)+ float(self.duration_time_entry_sec.get('1.0',"end-1c"))        
        self.end_time = (float(self.end_time_entry_min.get('1.0',"end-1c"))*60)+ float(self.end_time_entry_sec.get('1.0',"end-1c"))
        # calculate the times/duration
        self.time_valid = self.calc_duration()
        if self.time_valid:
            self.calc_min_sec()
            self.subclip_details_dict["start time"] = self.start_time
            self.subclip_details_dict["end time"] = self.end_time
            # pushes the values to widgets
            self.delete_time_entries()
            self.set_time_vals()
        

    def on_create_subclip_button(self,source_window):
        if self.time_valid:
            # open start frame
            self.first_frame_image_array = self.source_video.get_frame(self.start_time) 
            self.first_frame_image_location = Image.fromarray(self.first_frame_image_array)
            self.first_frame_image_resized = self.first_frame_image_location.resize((150,100))
            self.first_frame_image = ImageTk.PhotoImage(self.first_frame_image_resized)
            self.start_frame_label.config(image=self.first_frame_image)
            self.start_frame_label.image = self.first_frame_image
            # open end frame
            # Slight fix to the issue of the end time producing an error
            # self.end_frame_image_array = self.source_video.get_frame((self.end_time-.08)) 
            if self.end_time > (self.clip_time-.08):
                self.end_time = self.end_time-.08
            self.end_frame_image_array = self.source_video.get_frame((self.end_time)) 
            self.end_frame_image_location = Image.fromarray(self.end_frame_image_array)
            self.end_frame_image_resized = self.end_frame_image_location.resize((150,100))
            self.end_frame_image = ImageTk.PhotoImage(self.end_frame_image_resized)
            self.end_frame_label.config(image=self.end_frame_image)
            self.end_frame_label.image = self.end_frame_image

            self.number_of_subclips +=1
            self.subclip_name = self.clip_number_entry.get()
            self.subclip_details_dict["subclip name"] = self.subclip_name
            self.subclip_details_label_text = self.subclip_details_label_text +"\n Subclip : " +  self.subclip_details_dict["subclip name"] + " Start Time: " +str(self.subclip_details_dict["start time"])+" End Time: "+str(self.subclip_details_dict["end time"])
            self.subclip_details_label.config(text = self.subclip_details_label_text)
            self.clip_number_entry.delete(0,END)
            self.clip_number_entry.insert(0,str(self.number_of_subclips+1))

            print(self.subclip_details_dict)

            print("subclip created")
            
            source_window.subclip_dict_list.append(self.subclip_details_dict.copy())
            print(source_window.subclip_dict_list)
        else:
            self.subclip_info_label.config(text="Please enter valid times before creating clip",background='red')



    def calc_duration(self):
        # checks and validates start time/end time and calcs duration
        if self.start_time > 0:
            if self.end_time > 0:
                self.duration = self.end_time - self.start_time
            elif self.duration > 0:
                self.end_time = self.start_time + self.duration
            else:
                self.end_time = self.clip_time
                self.duration = self.end_time-self.start_time
        elif self.end_time > 0:
            if self.duration > 0:
                self.start_time = self.end_time - self.duration
            else:
                self.duration = self.end_time
        elif self.duration > 0:
            self.end_time =self.duration
        else:
            self.on_time_entry_reset_button()
            self.subclip_info_label.config(text="Duration is out of bounds",background='red')
            return False
        print(repr(self.end_time))
        # ensures time is within limits 
        if self.check_times() == False:
            return False
        else:
            self.subclip_info_label.config(text="Duration is within bounds",background='green')
            return True

        

        # sets minute and seconds values for each time
        
    
    def calc_min_sec(self):
        self.start_time_min = math.floor(self.start_time/60)
        self.start_time_sec = (self.start_time%60)
        
        self.duration_time_min = math.floor(self.duration/60)
        self.duration_time_sec = (self.duration%60)

        self.end_time_min = math.floor(self.end_time/60)
        self.end_time_sec = (self.end_time%60)

    def set_time_vals(self):
        # configures the time entries
        self.start_time_entry_min.insert('1.0',str(self.start_time_min))
        self.start_time_entry_sec.insert('1.0',str(self.start_time_sec))

        self.duration_time_entry_min.insert('1.0',str(self.duration_time_min))
        self.duration_time_entry_sec.insert('1.0',str(self.duration_time_sec))

        self.end_time_entry_min.insert('1.0',str(self.end_time_min))
        self.end_time_entry_sec.insert('1.0',str(self.end_time_sec))

    def delete_time_entries(self):
        # clears the time entries
        self.duration_time_entry_min.delete('1.0',END)
        self.duration_time_entry_sec.delete('1.0',END)
        self.end_time_entry_min.delete('1.0',END)
        self.end_time_entry_sec.delete('1.0',END)
        self.start_time_entry_min.delete('1.0',END)
        self.start_time_entry_sec.delete('1.0',END)

    def check_times(self):
        # checks times are within bounds
        if self.start_time <0 or self.duration <0 or self.end_time > self.clip_time:
            self.on_time_entry_reset_button()
            self.subclip_info_label.config(text="Time Error- Try again",background='red')
            return False
        else:
            return True


app = InitialWindow()
app.geometry("900x500")
app.mainloop()


# if app.athlete_name == "":
#             app.athlete_name = "Athlete"
print(app.athlete_name)
print(app.session_type)
print(app.export_video_date)