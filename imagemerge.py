#Evan Russenberger-Rosica
#Create a Grid/Matrix of Images
import PIL, os, glob
from PIL import Image
from math import ceil, floor
from PIL import ImageFont
from PIL import ImageDraw 
import pandas as pd
import math

Brands = ["ADIDAS","NIKE","FILA","CONVERSE","VANS","NEWBALANCE","PUMA","BIRKENSTOCK","SPERRY"]
#Brands = ["BIRKENSTOCK","SPERRY"]

for brand in Brands:
    df = pd.read_excel ("/Users/dm/Documents/PythonStudy/"+brand+".xlsx")

    for index, row in df.iterrows():

        #if index > 6:
        # PATH = "/Users/dm/Documents/PythonStudy/"+ str(row['Name']).strip() + "/" + str(index) + "_"
        PATH = "/Users/dm/Documents/PythonStudy/"+brand+"/DL_" + str(index) + "_"
        #print(PATH)
        images = glob.glob(PATH+"*")
        fulllist = images
        if len(fulllist) > 3:
            images = images[:5]                #get the first 30 images
            print(images)
            frame_width = 1920
            images_per_row = 3
            padding = 2

            img_width, img_height = Image.open(images[0]).size
            sf = (frame_width-(images_per_row-1)*padding)/(images_per_row*img_width)       #scaling factor
            scaled_img_width = ceil(img_width*sf)                   #s
            scaled_img_height = ceil(img_height*sf)

            number_of_rows = ceil(len(images)/images_per_row)
            frame_height = ceil(sf*img_height*number_of_rows) 

            new_im = Image.new('RGB', (frame_width, frame_height),(255,255,255))

            i,j=0,0
            for num, im in enumerate(images):
                if num%images_per_row==0:
                    i=0
                im = Image.open(im)
                #Here I resize my opened image, so it is no bigger than 100,100
                im.thumbnail((scaled_img_width,scaled_img_height))
                #Iterate through a 4 by 4 grid with 100 spacing, to place my image
                y_cord = (j//images_per_row)*scaled_img_height
                new_im.paste(im, (i,y_cord))
                #print(i, y_cord)
                i=(i+scaled_img_width)+padding
                j+=1

            draw = ImageDraw.Draw(new_im)
            font = ImageFont.truetype("/Users/dm/Documents/PythonStudy/AppleLiGothic-Medium.ttf", 90)
            font1 = ImageFont.truetype("/Users/dm/Documents/PythonStudy/AppleLiGothic-Medium.ttf", 30)
            font2 = ImageFont.truetype("/Users/dm/Documents/PythonStudy/AppleLiGothic-Medium.ttf", 50)
            draw.text((1300, 850),str(row['Name']).strip(),(0,0,0),font=font)
            #draw.text((1300, 920),"NOW: PHP "+str(row['Price']).strip(),(255,0,0),font=font)
            draw.text((1300, 920),"NOW: PHP "+str(row['Reseller']).strip(),(255,0,0),font=font)
            if len(str(row['OriginalPeso'])) > 1:
                if row['OriginalPeso'] > row['Price']:
                    draw.text((1300, 990),"JP STORE PRICE: PHP "+str(math.ceil(row['OriginalPeso'])).strip(),(0,0,0),font=font2)
            draw.text((20, 1230),str(row['SizesLabel']).strip(),(255,0,0),font=font1)
            
            #new_im.save("/Users/dm/Documents/PythonStudy/"+brand+"/" + "final_" + str(index) + ".jpg", "JPEG", quality=80, optimize=True, progressive=True)
            new_im.save("/Users/dm/Documents/PythonStudy/"+brand+"/" + "reseller_" + str(index) + ".jpg", "JPEG", quality=80, optimize=True, progressive=True)

            # # Iterate over the list of filepaths & remove each file.
            # for filePath in fulllist:
            #     try:
            #         os.remove(filePath)
            #     except:
            #         print("Error while deleting file : ", filePath)