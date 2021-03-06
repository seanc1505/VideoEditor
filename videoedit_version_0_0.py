from moviepy.editor import *

clip = VideoFileClip("20_11_22_freestyle.mp4") 
clip = clip.subclip(0, 35)
clip.ipython_display() 