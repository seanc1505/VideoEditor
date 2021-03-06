import tkinter as tk
from tkinter.constants import END
from typing import Text
from datetime import date, datetime
from PIL import ImageTk, Image  
import math

class SubclipWindow(tk.Tk):
    def __init__(self):
        tk.Toplevel.__init__(self)

        # Variable set up
        self.number_of_subclips=0
        self.subclip_name = ""
        self.time_calculated = False
    
        # Time Entry-Frame
        self.time_entry_frame = tk.Frame(self,relief=tk.RIDGE,borderwidth=5)
        self.define_subclip_gui_components()
        # Calculate time button
        self.time_entry_button = tk.Button(self.time_entry_frame, text="Calculate time", command=self.on_time_entry_button)
        # Reset time button
        self.time_entry_reset_button = tk.Button(self.time_entry_frame, text="Reset Times", command=self.on_time_entry_reset_button)
        # Create Subclip Button
        self.create_subclip_button = tk.Button(self.subclip_details_frame, text="Create Subclip", command=self.on_create_subclip_button)
        # Close button
        self.close_subclip_button = tk.Button(self, text="Close",background="orange", command=self.quit)
        self.place_subclip_gui_components()
        self.time_entry_frame.grid(row=1,column=0,columnspan=4)  
        
        
        
   
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
        self.start_time = (float(self.start_time_entry_min.get('1.0',"end-1c"))*60)+ float(self.start_time_entry_sec.get('1.0',"end-1c"))
        
        self.duration = (float(self.duration_time_entry_min.get('1.0',"end-1c"))*60)+ float(self.duration_time_entry_sec.get('1.0',"end-1c"))
        
        self.end_time = (float(self.end_time_entry_min.get('1.0',"end-1c"))*60)+ float(self.end_time_entry_sec.get('1.0',"end-1c"))
        
        self.calc_duration()

        self.number_of_subclips +=1
        self.subclip_name = self.clip_number_entry.get()
        # print(self.start_time)
        # print(self.end_time)
        # print(self.subclip_name)

    def on_create_subclip_button(self):
        self.first_frame_image_location = Image.open("ddd1.png")
        self.first_frame_image_location = self.first_frame_image_location.resize((150,100),Image.ANTIALIAS)
        self.first_frame_image = ImageTk.PhotoImage(self.first_frame_image_location)
        self.end_frame_image_location = Image.open("ddd2.png")
        self.end_frame_image_location  = self.end_frame_image_location.resize((150,100),Image.ANTIALIAS)
        self.end_frame_image = ImageTk.PhotoImage(self.end_frame_image_location)
        self.start_frame_label.config(image=self.first_frame_image)
        self.end_frame_label.config(image=self.end_frame_image)
        print("subclip created")


    def calc_duration(self):
        print(self.start_time)
        print(self.duration)
        print(self.end_time)
        if self.start_time > 0:
            if self.end_time > 0:
                self.duration = self.end_time - self.start_time
            elif self.duration > 0:
                self.end_time = self.start_time + self.duration
            else:
                # use end of clip
                self.end_time = 9999
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
            return
        
        self.delete_time_entries()
        
        self.start_time_min = math.floor(self.start_time/60)
        self.start_time_sec = (self.start_time%60)

        self.duration_time_min = math.floor(self.duration/60)
        self.duration_time_sec = (self.duration%60)

        self.end_time_min = math.floor(self.end_time/60)
        self.end_time_sec = (self.end_time%60)

        self.start_time_entry_min.insert('1.0',str(self.start_time_min))
        self.start_time_entry_sec.insert('1.0',str(self.start_time_sec))

        self.duration_time_entry_min.insert('1.0',str(self.duration_time_min))
        self.duration_time_entry_sec.insert('1.0',str(self.duration_time_sec))

        self.end_time_entry_min.insert('1.0',str(self.end_time_min))
        self.end_time_entry_sec.insert('1.0',str(self.end_time_sec))

        self.subclip_info_label.config(text="Duration is within bounds",background='green')
            
        

    def delete_time_entries(self):
        self.duration_time_entry_min.delete('1.0',END)
        self.duration_time_entry_sec.delete('1.0',END)
        self.end_time_entry_min.delete('1.0',END)
        self.end_time_entry_sec.delete('1.0',END)
        self.start_time_entry_min.delete('1.0',END)
        self.start_time_entry_sec.delete('1.0',END)


 


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
        self.source_video_duration = "Select clip"
        self.source_video_duration_opening_frame = "Select clip"
        self.source_video_image_location = Image.open("ddd.png")
        self.source_video_image_location = self.source_video_image_location.resize((250,200),Image.ANTIALIAS)
        self.source_video_image = ImageTk.PhotoImage(self.source_video_image_location)
        # Greeting Label
        self.greeting = tk.Label(text="Video Editing software V1")
        self.greeting.place(x=0,y=0)
        # Video Details frame
        self.export_video_details_frame = tk.Frame(relief=tk.RIDGE,borderwidth=10)
        # athlete name box
        self.athlete_name_frame = tk.Frame(self.export_video_details_frame,relief=tk.RIDGE,borderwidth=5,width=150,height=75)
        self.athlete_name_label= tk.Label(self.athlete_name_frame,text="Athlete Name: ")
        self.athlete_name_entry = tk.Entry(self.athlete_name_frame)
        
        self.athlete_name_label.grid(row = 0,column = 0)
        self.athlete_name_entry.grid(row = 0,column = 1)
        self.athlete_name_frame.grid(row=0,column=1)
        

        # Date Name Box
        self.video_date_frame = tk.Frame(self.export_video_details_frame,relief=tk.RIDGE,borderwidth=5,width=150,height=75)
        self.video_date_label= tk.Label(self.video_date_frame,text="Date: ")
        self.video_date_entry = tk.Entry(self.video_date_frame)
        self.video_date_entry.insert(0, self.export_video_date)
        self.video_date_label.grid(row = 0,column = 0)
        self.video_date_entry.grid(row = 0,column = 1)
        self.video_date_frame.grid(row=0,column=0)

        # Session type box
        self.session_type_frame = tk.Frame(self.export_video_details_frame,relief=tk.RIDGE,borderwidth=5,width=150,height=75)
        self.session_type_label= tk.Label(self.session_type_frame,text="Session type: ")
        self.session_type_entry = tk.Entry(self.session_type_frame)
        self.session_type_entry.insert(0, self.session_type)
        self.session_type_label.grid(row = 0,column = 0)
        self.session_type_entry.grid(row = 0,column = 1)
        self.session_type_frame.grid(row=0,column=3)


        self.export_video_name_button = tk.Button(self.export_video_details_frame, text="Export name Set", command=self.on_export_video_name_button)
        self.export_video_name_button.grid(row = 1,column = 0,columnspan=2)
        self.export_video_name_label = tk.Label(self.export_video_details_frame,text = "Video Name: " +self.export_video_name)
        self.export_video_name_label.grid(row=1,column=3)
        # Close button box
        self.close_button = tk.Button(self, text="Close",background="orange", command=self.quit)
        self.close_button.place(x=350,y=480)

        # Tutorial Button 
        self.tutorial_button = tk.Button(self,text="Need help? \nTutorial",background="orange" ,command=self.on_tutorial_button)
        self.tutorial_button.place(x=150,y=0)

        # New Subclip Button
        self.new_subclip_button = tk.Button(self,text="New Subclip",command=self.on_new_subclip_button)
        self.new_subclip_button.place(x=275,y=40)

        # Source video details frame
        self.source_video_details_frame = tk.Frame(relief=tk.RIDGE,borderwidth=5,width=150,height=150)
        # New source video button
        self.new_source_video_button = tk.Button(self.source_video_details_frame, text="New source video",background="green",font='Helvetica 12 bold', command=self.on_new_source_video_button)
        
        self.source_video_name_label = tk.Label(self.source_video_details_frame,text = self.source_video_name,borderwidth=5)
        self.video_name_label = tk.Label(self.source_video_details_frame,text = "Video name:",borderwidth=5)
        self.source_video_duration_label = tk.Label(self.source_video_details_frame,text = self.source_video_duration,borderwidth=5)
        self.video_duration_label = tk.Label(self.source_video_details_frame,text = "Video duration:",borderwidth=5)
        self.source_video_duration_opening_frame_label = tk.Label(self.source_video_details_frame,text = "Select Source video")
        self.new_source_video_button.grid(row=0,column=0)
        self.video_name_label.grid(row=1,column=0)
        self.source_video_name_label.grid(row=1,column=1)
        self.video_duration_label.grid(row=2,column=0)
        self.source_video_duration_label.grid(row=2,column=1)
        self.source_video_duration_opening_frame_label.grid(row=3,columnspan=2)
        self.source_video_details_frame.place(x=0, y=50)

        self.export_video_details_frame.place(x=0,y=350)

    def on_new_source_video_button(self):
        print("New window opened, find file")
        self.source_video_name = "GH10000"
        self.source_video_name_label.config(text=self.source_video_name)
        self.source_video_duration =  "00:03:10:14"
        self.source_video_duration_label.config(text=self.source_video_duration)
        self.source_video_duration_opening_frame = "Capture first frame and display here"
        self.source_video_duration_opening_frame_label.config(image=self.source_video_image)
        # Perform find file things

    def on_export_video_name_button(self):
        self.athlete_name = self.athlete_name_entry.get()
        self.export_video_date = self.video_date_entry.get()
        self.session_type = self.session_type_entry.get()
        self.export_video_name = self.export_video_date+ "_" + self.session_type + "_" + self.athlete_name 
        self.export_video_name_label.config(text="Video Name: " +self.export_video_name)

    def on_tutorial_button(self):
        print("Display Tutorial")
    def on_new_subclip_button(self):
        subclip = SubclipWindow()
        subclip.geometry("500x400")
        subclip.number_of_subclips =self.number_of_subclips
        subclip.mainloop()

app = InitialWindow()
app.geometry("700x500")
app.mainloop()


# if app.athlete_name == "":
#             app.athlete_name = "Athlete"
print(app.athlete_name)
print(app.session_type)
print(app.export_video_date)


    