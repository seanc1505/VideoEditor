from moviepy.editor import *
import scipy
clip = VideoFileClip("sample_video_clip.mp4") 
# clip = clip.subclip(0, 35)
# clip.ipython_display() 
duration = clip.duration
frame = clip.get_frame(3) 

frame = scipy.misc.imresize(frame, (50, 50))
print(frame)
