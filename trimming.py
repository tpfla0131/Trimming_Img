'''
image trimming
Used to remove blank areas around object in image.
Cropped images are always set to maintain square.

python=3.9
@rims
'''

import glob
import cv2
import os
from matplotlib import pyplot as plt

def squareCrop(imageDir):
    img = cv2.imread(imageDir)
    
    # find closed edge
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3,3), 0)
#    imgBin = cv2.threshold(imgBlur, 100, 255, cv2.THRESH_BINARY)[1]
    imgEdged = cv2.Canny(imgBlur, 10, 250)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (19,19))
    imgClosed = cv2.morphologyEx(imgEdged, cv2.MORPH_CLOSE, kernel)
    
    try:
        # find bounding box include contours
        contours = cv2.findContours(imgClosed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0][0]
        x,y,w,h = cv2.boundingRect(contours)
#        imgObject = cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2) #drawing line
        
        # resize bounding box as square
        HalfLine = max(w, h)/2+30 # padding 10pix
        center = (x+w/2, y+h/2)
        if HalfLine < 150 or HalfLine < img.shape[0] or HalfLine < img.shape[1]: # input by nn standard 256pix
            return img
        else:
            x1 = center[0] - HalfLine
            if x1<0: x1=0
            y1 = center[1] - HalfLine 
            if y1<0: y1=0
    
#            imgSquare = cv2.rectangle(img, (int(x1),int(y1)), 
#                                 (int(center[0]+HalfLine),int(center[1]+HalfLine)), (255,0,0), 2)
            
            imgCrop = img[int(y1):int(center[1]+HalfLine), 
                          int(x1):int(center[0]+HalfLine)]
             
            if all(imgCrop .shape) == False:
                return img
            else:
                return imgCrop
    except IndexError:
        return img

def createFolder(basePath, folderName):
    if os.path.exists(os.path.join(basePath, folderName)):
        folderPath = os.path.join(basePath, folderName)
    else:
        folderPath = os.makedirs(os.path.join(basePath, folderName))
        folderPath = os.path.join(basePath, folderName)
    
    return str(folderPath)

# create folder for saving a cropped image     
baseDir = r'C:\Users\tpfla\Desktop\DataCreate'
dataImgDir = os.path.join(baseDir, 'Dataset')
cropImgDir = createFolder(baseDir, 'CropData')

# save cropped image
for uf in os.listdir(dataImgDir):
    for im in os.listdir(os.path.join(dataImgDir, uf)):
        cropIndexDir = createFolder(cropImgDir, 'crop_{}'.format(uf))
        imgName = os.path.join(dataImgDir, uf, im)
        cropImg = squareCrop(imgName)
        if not os.path.exists(os.path.join(cropIndexDir, im[:-4]+'_crop.png')):
            cv2.imwrite(os.path.join(cropIndexDir, im[:-4]+'_crop.png'), cropImg)
        else:
            pass
    print('Finish {}'.format(uf))