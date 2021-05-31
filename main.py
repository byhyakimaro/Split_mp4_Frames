import cv2
import os

video = input(str('Video: '))
vidcap = cv2.VideoCapture(video)
success,image = vidcap.read()
os.mkdir('frames')
count = 0

while success:
  cv2.imwrite("frames/frame%d.png" % count, image)      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1