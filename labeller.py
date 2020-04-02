import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2
from win32api import GetSystemMetrics
from tkinter import *
import shutil

cwd = os.getcwd()
# print(cwd)
# os.mkdir(cwd+'/1')
# os.mkdir(cwd+'/0')
def callback(img):
    print(img+" "+e.get())
    if e.get() == '1':
        shutil.copy('celegans_training_set_super_cropped/'+img, '1')
    else:
        shutil.copy('celegans_training_set_super_cropped/'+img, '0')
    
    # os.rename('celegans_training_set_super_cropped/'+img,img.split('.')[0]+'_'+e.get()+".png")

images = list(filter(lambda x : x.split('.')[-1] == 'png',os.listdir('celegans_training_set_super_cropped')))

def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)

for img in images:
    # break
    num = img.split('_')[1].split('.')[0]
    # print(num)
    if int(num) < 2917 or int(num) > 3820: # Change to your assigned numbers
        continue
    master = Tk()
    e = Entry(master)
    e.pack()

    e.focus_set()
    b = Button(master, text = "OK", width = 10, command = lambda : callback(img))
   
    b.pack()
    frame = cv2.imread('celegans_training_set_super_cropped/'+img, 1)
    resize = ResizeWithAspectRatio(frame, height=GetSystemMetrics(1)-200) 
    cv2.imshow('output', resize)
    mainloop()
    key = cv2.waitKey(0)
    if key == 27:#if ESC is pressed, exit loop
        cv2.destroyAllWindows()
        break
    # print("Outside",e.get())
    
# OK, Cross, Space