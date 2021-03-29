import cv2     # for capturing videos
import math   # for mathematical operations
import matplotlib.pyplot as plt    # for plotting the images
# % matplotlib inline
import pandas as pd
from keras.preprocessing import image   # for preprocessing the images
import numpy as np    # for mathematical operations
from keras.utils import np_utils
from skimage.transform import resize   # for resizing images
from sklearn.model_selection import train_test_split
from glob import glob
from tqdm import tqdm


# # open the .txt file which have names of training videos
# f = open("trainlist01.txt", "r")
# temp = f.read()
# videos = temp.split('\n')

# # creating a dataframe having video names
# train = pd.DataFrame()
# train['video_name'] = videos
# train = train[:-1]
# train.head()


# # open the .txt file which have names of test videos
# f = open("testlist01.txt", "r")
# temp = f.read()
# videos = temp.split('\n')

# # creating a dataframe having video names
# test = pd.DataFrame()
# test['video_name'] = videos
# test = test[:-1]
# test.head()

# # storing the frames from training videos
# for i in tqdm(range(train.shape[0])):
#     count = 0
#     videoFile = train['video_name'][i]
#     cap = cv2.VideoCapture('UCF/'+videoFile.split(' ')[0].split('/')[1])   # capturing the video from the given path
#     frameRate = cap.get(5) #frame rate
#     x=1
#     while(cap.isOpened()):
#         frameId = cap.get(1) #current frame number
#         ret, frame = cap.read()
#         if (ret != True):
#             break
#         if (frameId % math.floor(frameRate) == 0):
#             # storing the frames in a new folder named train_1
#             filename ='train_1/' + videoFile.split('/')[1].split(' ')[0] +"_frame%d.jpg" % count;count+=1
#             cv2.imwrite(filename, frame)
#     cap.release()