import pandas as pd
import requests
import os
import numpy as np
import glob
from PIL import Image
from math import ceil, floor
from PIL import ImageFont
from PIL import ImageDraw 
import cv2
import numpy as n

PATH = "/Users/dm/Documents/PythonStudy/ALLPRODUCTS/"
images = glob.glob(PATH+"*.jpg")
images.sort(key=os.path.getmtime)

for imageload in images:
    # Load image, convert to grayscale, Gaussian blur, Otsu's threshold
    image = cv2.imread(imageload)
    original = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Obtain bounding rectangle and extract ROI
    x,y,w,h = cv2.boundingRect(thresh)
    cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
    ROI = original[y:y+h, x:x+w]

    # Add alpha channel
    b,g,r = cv2.split(ROI)
    alpha = np.ones(b.shape, dtype=b.dtype) * 50
    ROI = cv2.merge([b,g,r,alpha])

    #cv2.imshow('ROI', ROI)
    cv2.imwrite(imageload, ROI) 

# df = pd.read_excel ("Japan_Needs.xlsx")

# categories = ["Chocolates","Hair","Face","Watch","Soup","Vitamin","Snack","Electronics","Food","Noodle"]

# for category in categories:
#     os.mkdir(category)

# for index, row in df.iterrows():

#     if len(str(row["Imgs"])) > 3:
#         image = "ALLPRODUCTS/"+str(row["Code"])+"_1.jpg"
#         print(image)
#         maximimum = 885, 640
#         #100,200
#         #maximimum = 790, 668

#         #im1 = Image.open('Product Template.jpg')
#         im1 = Image.open('ProductTemplate.jpg')
#         imagesave = str(row["Category"])+"/"+str(row["Code"])+".jpg"

#         im2 = Image.open(image)
#         im2.thumbnail(maximimum, Image.ANTIALIAS)
#         width, height = im2.size
#         im1.paste(im2, (58+int((maximimum[0]-width)/2), 192+int((maximimum[1]-height)/2)))
#         #im1.paste(im2, (100+int((maximimum[0]-width)/2), 40+int((maximimum[1]-height)/2)))
#         draw = ImageDraw.Draw(im1)
#         font = ImageFont.truetype("/Users/dm/Documents/PythonStudy/AppleLiGothic-Medium.ttf", 60)
#         font1 = ImageFont.truetype("/Users/dm/Documents/PythonStudy/AppleLiGothic-Medium.ttf", 50)
#         draw.text((58, 875),str(row['Name']).strip(),(0,0,0),font=font)
#         #draw.text((660, 790),"PHP "+str(int(row['SRP'])).strip(),(255,0,0),font=font)
#         #draw.text((100, 790),"PHP "+str(int(row['RRP'])).strip(),(255,0,0),font=font)
#         im1.save(imagesave, "JPEG")
#         #im1.show()
        

        #DOWNLOAD IMAGES
        # y = 0
        # print(row['Imgs'])
        # if len(str(row['Imgs']))>5:
        #     listofurl = row['Imgs'].split(",")
        #     print(listofurl)
        #     if len(listofurl)>0:
        #         for i in listofurl:
        #             y += 1
        #             print(i)
        #             print(row['Code'].strip()+".jpg")
                    # response = requests.get(i)
                    # file = open("ALLPRODUCTS/"+row['Code'].strip()+"_"+str(y)+".jpg", "wb")
                    # file.write(response.content)
                    # file.close()